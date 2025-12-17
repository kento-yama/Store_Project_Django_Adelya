from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('order/', views.order, name='order'),
    path('orders/', views.orders_list, name='orders'),
    path('create/', views.order_create, name='create'),
    path('success/', views.success, name='success'),
]
