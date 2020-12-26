from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest
from .forms import SlotForm
from ticket.models import Slot
from django.contrib.auth.decorators import login_required
from basic.decorators import allowed_users,admin_only
# Create your views here.

@login_required(login_url='/login')
@admin_only
def slot(request):
    slot = Slot.objects.all()
    return render(request,'slot/slot.html',{'slot':slot})

@login_required(login_url='/login')
@admin_only
def createSlot(request):
    form = SlotForm()
    if request.method == 'POST':
        a = request.POST['slot_name']
        a = a.upper()
        slot = Slot.objects.filter(slot_name = a)
        if len(slot)<1:
            form = SlotForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/slot')
        return render(request,'slot/new_slot.html',{'form':form,'message':'Same Slot name exists'})
    return render(request,'slot/new_slot.html',{'form':form})

@login_required(login_url='/login')
@admin_only
def updateSlot(request,pk):
    slot = Slot.objects.get(slot_id=pk)
    form = SlotForm(instance=slot)
    if request.method == 'POST':
        a = request.POST['slot_name']
        a = a.upper()
        slot1 = Slot.objects.filter(slot_name = a)
        if len(slot1)<2:
            form = SlotForm(request.POST,instance=slot)
            if form.is_valid():
                form.save() 
                return redirect('/slot')
        return render(request,'slot/new_slot.html',{'form':form,'message':'Same slot name exist or you cant change existing name of slot'})
    return render(request,'slot/new_slot.html',{'form':form})

@login_required(login_url='/login')
@admin_only
def deleteSlot(request,pk):
    slot = Slot.objects.get(slot_id=pk)
    if request.method == 'POST':
        slot.delete()
        return redirect('/slot')
    return render(request,'slot/delete_slot.html',{'name':slot})