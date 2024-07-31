from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.template.loader import render_to_string
from .models import Companys, Tags, Product, Sizes
from django.views.generic import ListView, TemplateView,DetailView, FormView
#from .forms import Authentication
from django.urls import reverse, reverse_lazy
from cart import forms
from cart.forms import CartAddProductForm
from cart.cart import Cart

from .utils import DataMixin

tag_data = Tags.objects.all()


def empty(request):
    return redirect('lending:home')


class Home(TemplateView):
    template_name = 'home_page.html'
    extra_context = {'title' : 'Home'}




class About_usList(ListView):
    paginate_by = 3
    model = Companys
    template_name = 'about_us.html'
    context_object_name = 'companys'
    extra_context = {'title': 'About Us'}





class ProductList(DataMixin,ListView):
    paginate_by = 3
    template_name = 'products_list.html'
    context_object_name = 'products'
    title_page = 'Products'
    #extra_context = {'title': 'Products','cart_product_form': CartAddProductForm()}


    def get_queryset(self) -> QuerySet[Any]:
        return Product.product.filter(Maker = Companys.objects.get(slug = self.kwargs['slugy']))


class CatalogView(DataMixin,ListView):
    title_page = 'Catalog'
    paginate_by = 3
    template_name = 'catalog.html'
    model = Product
    context_object_name = 'products'
    #extra_context = {'form' : CartAddProductForm()}

    def get_queryset(self):
        products = Product.objects.filter(stock = 1)
        if 'size' in self.request.GET:
            size = Sizes.objects.get(name = self.request.GET['size'])
            products = size.products.all()

        if 'kind' in self.request.GET:
            kind = Tags.objects.get(name = self.request.GET['kind'])
            products = products.filter(tags__slug = self.request.GET['kind'])

        if 'creator' in self.request.GET:
            products = products.filter(Maker_id__slug = self.request.GET['creator'])

        if 'sex' in self.request.GET:
            products = products.filter(tags__slug = self.request.GET['sex'])

        return products


class SaleView(DataMixin,ListView):
    title_page = 'Sale'
    paginate_by = 3
    template_name = 'sale.html'
    context_object_name = 'products'


    def get_queryset(self):
        return Product.objects.filter(tags__pk = 8)





class ProductView(DataMixin,FormView):
    template_name = 'productPage.html'
    form_class = CartAddProductForm


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(pk = self.kwargs['pk'])
        context['title'] = Product.objects.get(pk = self.kwargs['pk']).productModel
        return context
    
   

    

