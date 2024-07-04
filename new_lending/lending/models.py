from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import uuid


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
        return reverse('products_list', kwargs= {'slugy' : self.slug})
    
    class Meta:
        verbose_name = "Companys"
        verbose_name_plural = "Companys"

class Product(models.Model):

    class Status(models.IntegerChoices):

        inStock = 1, 'In stock'
        outStock = 0, 'Out stock'


    productModel = models.CharField(max_length= 255,verbose_name="Product")
    descripton = models.TextField(max_length=255, default='any description')
    image = models.ImageField(blank= True)
    sizesAndTheirCount= models.CharField(max_length= 255, blank = True)
    id = models.UUIDField(unique= True,blank= False, default= uuid.uuid4,primary_key=True)
    Maker = models.ForeignKey('Companys', on_delete= models.PROTECT,null=True,related_name='maker')
    stock = models.IntegerField(choices= Status.choices)
    cost = models.IntegerField(null= True)
    tags = models.ManyToManyField('Tags', blank = True, related_name= 'tag')
    photo = models.ImageField(upload_to= 'photos/%Y/%m/%d', blank= True, null= True, verbose_name='photo')

    
    objects = models.Manager()
    product = inStockProduct()

    def __str__(self) -> str:
        return self.productModel

    def get_absolute_url(self):
        return reverse('product_page', kwargs={'pk' : self.id})
    
    class Meta:
        ordering = ['-cost']
        indexes = [
            models.Index(fields=['-cost'])
        ]


class Users(models.Model):

    name = models.CharField(max_length=32,blank=True)
    surname = models.CharField(max_length=32,blank=True)
    login = models.CharField(max_length=18)
    password = models.CharField(max_length=32)
    phoneNumber = models.CharField(max_length=12)
    country = models.CharField(max_length=32)
    mail = models.EmailField()
    adressToOrder = models.TextField(max_length=256,blank=True)

    def __str__(self):
        return self.mail


class usersOrders(models.Model):

    class orderStatus(models.IntegerChoices):
        orderAdopted = 0, 'Adopted'
        orderAssebmbled = 1, 'Assembled'
        orderSended = 2, 'Sended'
        orderDelivered = 3, 'Delivered'

    orderPositions = models.JSONField(blank=False)
    userLogin = models.ForeignKey('Users', on_delete= models.PROTECT)
    status = models.IntegerField(blank= False, null= True, choices= orderStatus.choices)
    receipt = models.OneToOneField('Transactions',blank= False, null= True, on_delete= models.PROTECT,related_name='userOrders')
    


class Transactions(models.Model):

    class transactionStatus(models.IntegerChoices):
        transactionsRejected = 0, 'Rejected'
        transactionAccepted = 1, 'Accepted'

    user = models.OneToOneField('Users', blank= False, null = True, on_delete= models.PROTECT, related_name= 'Transactions')
    id = models.UUIDField(blank= False, primary_key= True,unique= True, default= uuid.uuid4)
    amount = models.IntegerField(blank= False, null= True)
    receipt = models.ImageField(null= True)

    def __str__(self):
        return self.id

class Tags(models.Model):
    name = models.CharField(max_length= 100)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_slug(self):
        return slugify(self.name, allow_unicode= True)
    
    def get_absolute_url(self):
        return reverse('catalog', kwargs= {'tag' : self.slug})


