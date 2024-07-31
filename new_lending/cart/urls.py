from django.urls import path, include, re_path

from . import views
app_name = 'cart'

urlpatterns = [
    path('add_to_cart/<uuid:product_id>/', views.AddCart.as_view(), name = 'cart_add'),
    path('details/', views.Details.as_view(), name='details'),
    path('order/done/', views.TakeOrder.as_view(), name = 'order_done'),
    path('order/information/', views.TypeOrderInformation.as_view(), name = 'order_information'),
    path('order/<uuid:order_id>', views.OrderView.as_view(), name = 'order')
]