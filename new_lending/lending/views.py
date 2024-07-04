from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.template.loader import render_to_string
from lending.models import Companys, Product, Tags, Users
from django.views.generic import ListView, TemplateView,DetailView, FormView
from .forms import Authentication
from django.urls import reverse, reverse_lazy
from .utils import DataMixin

tag_data = Tags.objects.all()






# def home_page(request):
#     data = {
#         'tags' : tag_data
#     }
#     return render(request,'home_page.html',data)
class Home(DataMixin, TemplateView):
    template_name = 'home_page.html'
    


def redirecting(request):
    return redirect('home')

def catalog(request):
    data = {
        'tags' : tag_data
    }
    return render(request,'catalog.html',data)

def sale(request):
    data = {
        'tags' : tag_data
    }
    return render(request, 'sale.html',data)


class PartnersList(DataMixin, ListView):
    model = Companys
    template_name = 'partners.html'
    context_object_name = 'companys'

    


class ProductList(DataMixin, ListView):
    template_name = 'products_list.html'
    context_object_name = 'products'


    def get_queryset(self) -> QuerySet[Any]:
        return Product.product.filter(Maker = Companys.objects.get(slug = self.kwargs['slugy']))
        
        



class ProductView(DataMixin, DetailView):

    template_name = 'productPage.html'
    model = Product


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(pk = self.kwargs['pk'])
        return context
    
   


def authentication(request):
    data = {
        'tags' : tag_data
    }
    return render(request, 'authentication.html',context=data)


class Authentication(DataMixin, FormView):
    model = Users
    form_class = Authentication
    template_name = 'authentication.html'
    success_url = reverse_lazy('home')

    

