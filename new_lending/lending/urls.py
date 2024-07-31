from django.urls import path, include, re_path
from . import views
from django.contrib import admin

app_name = 'lending'

urlpatterns = [
    path('',views.empty, name = "empty"),
    path('home/',views.Home.as_view(), name= "home"),
    path('catalog/', views.CatalogView.as_view(), name = "catalog"),
    path('sale/',views.SaleView.as_view(), name = 'sale'),
    path('partners/',views.About_usList.as_view(), name ='about_us'),
    path('partners/<slug:slugy>/', views.ProductList.as_view(),name = 'products_list'),
    path('product/<uuid:pk>/',views.ProductView.as_view(), name = 'product_page'),
]