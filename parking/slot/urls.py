from django.urls import path
from . import views


urlpatterns = [
    path('', views.slot,name="slot"),
    path('createSlot/',views.createSlot,name='createSlot'),
    path('updateSlot/<str:pk>/',views.updateSlot,name='updateSlot'),
    path('deleteSlot/<str:pk>/',views.deleteSlot,name='deleteSlot'),
]