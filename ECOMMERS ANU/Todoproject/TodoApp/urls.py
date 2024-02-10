from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name='home'),
    path('details/<int:id>',views.Details,name='details'),
    path('smart/<str:cat>',views.Smart,name='smart'),
    path('addcart/<int:id>',views.addcart,name='addcart'),
    path('cart/',views.cart,name='cart'),
    path('delete/<int:id>',views.delete,name='delete'),
     


]
