from django.urls import path,include
from lending import views
from django.contrib import admin

urlpatterns = [
    path('home/',views.Home.as_view(), name= "home"),
    path('',views.redirecting, name="empty"),
    path('catalog/', views.catalog, name = "catalog"),
    path('sale/',views.sale, name = 'sale'),
    path('partners/',views.PartnersList.as_view(), name ='partners'),
    path('partners/<slug:slugy>/', views.ProductList.as_view(),name = 'products_list'),
    path('product/<uuid:pk>/',views.ProductView.as_view(), name = 'product_page'),
    path('authentication/',views.Authentication.as_view(), name = 'authentication'),
    #path('product/<slug:tag>/',views.productPage, name = 'product_page'),
]