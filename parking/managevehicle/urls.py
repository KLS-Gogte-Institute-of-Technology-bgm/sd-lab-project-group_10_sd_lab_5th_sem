from django.urls import path
from managevehicle import views

urlpatterns = [
    path('', views.manage_vehicle),
    path('updateTicket/<str:pk>',views.updateTicket,name='updateTicket'),
]