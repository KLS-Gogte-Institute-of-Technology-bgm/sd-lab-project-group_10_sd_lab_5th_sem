from django.urls import path
from ticket import views

urlpatterns = [
    path('', views.ticket),
    path('createTicket',views.createTicket,name='createTicket'),
    path('createSLot',views.createSlot,name='createSlot')
]