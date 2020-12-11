from django.urls import path
from searchvehicle.views import search_vehicle

urlpatterns = [
    path('', search_vehicle),
]