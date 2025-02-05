from django.urls import path 
from . import views

urlpatterns = [ 
    path('carlist/', views.carlist, name='carlist'),
    path('<int:pk>/', views.cardetails, name='carlist'),    

]
