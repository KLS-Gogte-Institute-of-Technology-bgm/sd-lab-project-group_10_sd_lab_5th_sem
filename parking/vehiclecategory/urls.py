from django.urls import path
from vehiclecategory.views import vehicle_category,vehicle_category_unique_update,createCategory,deleteCategory

urlpatterns = [
    path('', vehicle_category,name="vehicle_category"),
    path('<str:pk>/', vehicle_category_unique_update,name="vehicle_category_unique"),
    path('deleteCategory/<str:pk>/', deleteCategory,name="deleteCategory"),
    path('createCategory',createCategory,name='createCategory')
]