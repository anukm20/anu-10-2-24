from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name='home'),
    path('newcontact/',views.Newcontact,name='newcontact'),
    
]