from django.forms import ModelForm
from django.forms import fields
from .models import Category

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'