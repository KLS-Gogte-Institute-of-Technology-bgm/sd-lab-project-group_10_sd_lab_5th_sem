from django.shortcuts import render,redirect
from django.http import HttpResponse
from vehiclecategory.models import Category
from .form import CategoryForm
from django.contrib.auth.decorators import login_required
from basic.decorators import allowed_users,admin_only
# Create your views here.

@login_required(login_url='/login')
@admin_only
def vehicle_category(request):
    category = Category.objects.all().order_by('category_id')
    return render(request,'vehiclecategory/vehicle_category.html',{'category':category})

@login_required(login_url='/login')
@admin_only
def vehicle_category_unique_update(request,pk):
    category = Category.objects.get(category_id=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form  = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('/vehiclecategory')
    return render(request,'vehiclecategory/new_category.html',{'form':form})

@login_required(login_url='/login')
@admin_only
def createCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form  = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/vehiclecategory')
    return render(request,'vehiclecategory/new_category.html',{'form':form})

@login_required(login_url='/login')
@admin_only
def deleteCategory(request,pk):
    category = Category.objects.get(category_id=pk)
    name = category.type
    if request.method == 'POST':
        category.delete()
        return redirect('/vehiclecategory')
    context={'name':name}
    return render(request,'vehiclecategory/delete_category.html',context)
 