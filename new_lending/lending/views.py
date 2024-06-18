from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.template.loader import render_to_string
from lending.models import Companys,Product, Tags




def home_page(request):
    text_data ={
        'text': "Hello it's my first website, don't judge, please",
        'tags' : Tags.objects.all()
    }
    return render(request,'home_page.html',text_data)

def redirecting(request):
    return redirect('home')

def catalog(request):
    return render(request,'catalog.html')

def sale(request):
    return render(request, 'sale.html')

def partners(request):
    data = {'companys' : Companys.objects.all()}
    return render(request,'partners.html',context = data)

def products_list(request,slugy):
    data = {
        'products' :  Product.product.filter(Maker = Companys.objects.get(slug = slugy).nameOfCopmany),
    }
    return render(request,'products_list.html',context = data)

def productPage(request,id):
    data = {
        'product' : Product.objects.get(pk = id)
    }
    print(id,Product.objects.get(pk = id))
    return render(request,'productPage.html', context=data)