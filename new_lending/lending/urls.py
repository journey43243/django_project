from django.urls import path,include
from lending import views
from django.contrib import admin

urlpatterns = [
    path('admin',admin.site.urls),
    path('home/',views.home_page, name= "home"),
    path('',views.redirecting, name="empty"),
    path('catalog/', views.catalog, name = "catalog"),
    path('sale/',views.sale, name = 'sale'),
    path('partners/',views.partners, name ='partners'), #views.partners,name ='partners'
    path('partners/<slug:slugy>/', views.products_list,name = 'products_list'),
    path('product/<uuid:id>/',views.productPage, name = 'product_page')
   # path('sale/<slug:id>/', views.products_list, name = 'products_list')
]