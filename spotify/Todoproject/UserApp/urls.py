from django.urls import path
from . import views
app_name='auth'
urlpatterns = [
    path('signup',views.Signup,name='signup'),
    
]
