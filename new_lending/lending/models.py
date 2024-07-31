from functools import partial
from django import utils
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import uuid
import json

from new_lending import settings


class inStockProduct(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(stock = 1)

class Companys(models.Model):
    nameOfCopmany = models.CharField(primary_key= True,max_length= 30,verbose_name='Name')
    Descripton = models.TextField(max_length=255, verbose_name= 'Description')
    image = models.ImageField()
    slug = models.SlugField(blank= False, unique= True)
     
    
    def __str__(self) -> str:
        return self.nameOfCopmany

    def get_absolute_url(self):
        return reverse('lending:products_list', kwargs= {'slugy' : self.slug})
    
    class Meta:
        verbose_name = "Companys"
        verbose_name_plural = "Companys"

class Product(models.Model):

    class Status(models.IntegerChoices):

        inStock = 1, 'In stock'
        outStock = 0, 'Out stock'


    productModel = models.CharField(max_length= 255,verbose_name="Product")
    descripton = models.TextField(max_length=255, default='any description')
    id = models.UUIDField(unique= True,blank= False, default= uuid.uuid4,primary_key=True)
    Maker = models.ForeignKey('Companys', on_delete= models.PROTECT,null=True,related_name='maker')
    stock = models.IntegerField(choices= Status.choices)
    cost = models.IntegerField(null= False)
    tags = models.ManyToManyField('Tags', blank = True, related_name= 'tag')
    photo = models.ImageField(upload_to= 'photos/%Y/%m/%d', blank= True, null= True, verbose_name='photo')


    objects = models.Manager()
    product = inStockProduct()

    def __str__(self) -> str:
        return self.productModel

    def get_absolute_url(self):
        return reverse('lending:product_page', kwargs={'pk' : self.id})

    class Meta:
        ordering = ['-cost']
        indexes = [
            models.Index(fields=['-cost'])
        ]




class usersOrders(models.Model):

    class orderStatus(models.IntegerChoices):
        orderAdopted = 0, 'Adopted'
        orderAssebmbled = 1, 'Assembled'
        orderSended = 2, 'Sended'
        orderDelivered = 3, 'Delivered'

    orderPositions = models.ManyToManyField('Product', blank=False, related_name='products', null= True)
    userLogin = models.ForeignKey('User', on_delete= models.PROTECT)
    order_name = models.CharField(max_length=64, blank= False, verbose_name='Name')
    order_surname = models.CharField(max_length=64, blank= False)
    order_second_name = models.CharField(max_length=64, blank= False)
    order_phone = models.CharField(max_length=64, blank= False)
    order_place = models.CharField(max_length=64, blank=False)
    status = models.IntegerField(blank= False, choices= orderStatus.choices)
    receipt = models.ImageField(blank= False)
    cart_url = models.CharField(blank= False)
    id = models.UUIDField(primary_key=True, blank=False,default=uuid.uuid4, unique=True)
    quantities = models.CharField(null= False, blank= False)
    



class Tags(models.Model):
    name = models.CharField(max_length= 100)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_slug(self):
        return slugify(self.name, allow_unicode= True)

    def get_absolute_url(self):
        return reverse('lending:catalog', kwargs= {'tag' : self.slug})


class Sizes(models.Model):
    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=2)
    products = models.ManyToManyField('Product', related_name='sizes')




class User(AbstractUser):


    def get_password_reset_url(self):
        base64_encoded_id = utils.http.urlsafe_base64_encode(utils.encoding.force_bytes(self.id))
        token = PasswordResetTokenGenerator().make_token(self)
        reset_url_args = {'uidb64': base64_encoded_id, 'token': token}
        reset_path = reverse('authentication:password_reset_confirm', kwargs=reset_url_args)
        reset_url = f'{settings.BASE_URL}{reset_path}'
        return reset_url