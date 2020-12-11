from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage,name='registerPage'),
    path('', views.loginPage,name='loginPage'),
    path('login/', views.loginPage,name='loginPage'),
    path('logout/', views.logoutPage,name='logoutPage'),
    path('user/',views.userPage,name='userPage'),
    path('myTicket/',views.myTicket,name='myTicket')
]
