from django.urls import path
from analysis import views

urlpatterns = [
    path('', views.analysis),
]