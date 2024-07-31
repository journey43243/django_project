import json
import ast
import qrcode
from django.contrib.auth import get_user, get_user_model
from django.urls import reverse
from fpdf import FPDF
from lending.models import usersOrders
from lending.models import Product
import os

class CreateOrder:

    @classmethod
    def create_pdf(cls,number):

        pdf = FPDF()
        pdf.add_page()
        img = qrcode.make('http://127.0.0.1:8000/order/done/')
        save_url = f'media/qrs/qr_{number}.jpeg'
        img.save(save_url)
        pdf.image(save_url)
        pdf.output(f'media/orders/order_{number}.pdf')
        os.remove(save_url)

        return f'media/orders/order_{number}.pdf'

    @classmethod
    def create_order(cls, request, pdf, id):
        user = get_user_model().objects.get(username = get_user(request).username)
        status = usersOrders.orderStatus.orderAdopted
        receipt = pdf
        id = id
        cart_url = reverse('cart:order', kwargs = {'order_id' : id})
        order_name = request.POST['name']
        order_surname = request.POST['surname']
        order_second_name = request.POST['second_name']
        order_phone = request.POST['phone_number']
        order_place = request.POST['order_place']
        order = usersOrders.objects.create(userLogin = user,status = status, receipt = receipt,id = id, cart_url = cart_url,
                                           order_name = order_name, order_surname = order_surname,
                                           order_second_name = order_second_name, order_phone = order_phone,
                                           order_place = order_place)
        order.save()
        quant = {}
        for product, item in request.session['cart'].items():
            order.orderPositions.add(product)
            quant[product] = item['quantity']
        print(quant)
        order.quantities = quant
        order.save()
