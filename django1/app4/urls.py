from django.urls import path
from . import views 
#from app3.views import home

urlpatterns = [
    path('home/', views.home, name='home'),
    #path('', views.index, name='index'),

]
