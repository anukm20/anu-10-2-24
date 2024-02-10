from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('des/',views.des,name='des'),
    path('ele/',views.ele,name='ele'),
    path('news/',views.news,name='news')
]
