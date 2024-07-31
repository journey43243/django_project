import ast
import json
import uuid

from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.decorators.http import require_POST
from django.views.generic import FormView, ListView, DetailView, TemplateView
from lending.models import Product

from .CreateOrder import CreateOrder
from .cart import Cart
from .forms import CartAddProductForm, OrderInformation
from new_lending import settings

from lending.models import usersOrders


class AddCart(LoginRequiredMixin,FormView):
    form_class = CartAddProductForm

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        cart.add(product_id= str(self.kwargs['product_id']),
                 quantity=request.POST['quantity'],
                 update_quantity=request.POST['update'])
        return redirect('cart:details')

class Details(LoginRequiredMixin,ListView):
    model = Product
    template_name = 'cart.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        cart = Cart(self.request)
        context['cart'] = cart.cart
        context['total_cost'] = str(cart.get_total_price())
        return context

class TakeOrder(LoginRequiredMixin,FormView):
    template_name = 'takeorder.html'


    def post(self, request, *args, **kwargs):
        order = CreateOrder
        order_id = str(uuid.uuid4())
        order_url = order.create_pdf(number= order_id)
        email = EmailMessage(
            "Order Information",
            "In this file you can this all information about order",
            f"{settings.EMAIL_HOST_USER}",
            [f"{get_user(request).email}"],
        )
        email.attach_file(order_url)
        email.send()
        order.create_order(pdf = order_url, request=request, id = order_id)
        request.session['cart'] = {}

        return redirect('lending:home')


class OrderView(LoginRequiredMixin, TemplateView):
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        order = usersOrders.objects.get(pk = self.kwargs['order_id'])
        context['order_positions'] = order.orderPositions.all()
        context['order_quantities'] = ast.literal_eval(order.quantities)
        context['total_price'] = 0

        for product in context['order_positions']:
            context['total_price'] += product.cost * int(context['order_quantities'].get(str(product.id)))

        return context


class TypeOrderInformation(LoginRequiredMixin, FormView):

    form_class = OrderInformation
    template_name = 'order_information.html'
