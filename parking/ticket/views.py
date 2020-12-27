from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Slot,Ticket
from .form import TicketForm,SlotForm
from django.contrib.auth.decorators import login_required
from basic.decorators import allowed_users,admin_only
# Create your views here.

@login_required(login_url='/login')
@allowed_users(allowed_roles=['manager','watchman','customer'])
def ticket(request):
    total_slot = Slot.objects.count()
    parked = Ticket.objects.filter(slot_active = True).count()
    slot_left = total_slot-parked
    context = {'total_slot':total_slot,'parked':parked,'slot_left':slot_left}
    return render(request,'ticket/ticket.html',context)

@login_required(login_url='/login')
@allowed_users(allowed_roles=['manager','watchman','customer'])
def createTicket(request):
    form = TicketForm()
    slot_left = Slot.objects.all()
    slot_reght = Ticket.objects.all().filter(slot_active=True)
    ls = []
    for i in slot_left:
        a = str(i)
        ls.append(a)
    for j in slot_reght:
        b = str(j)
        try:
            ls.remove(b)
        except:
            pass
    if request.method == 'POST':
        form  = TicketForm(request.POST)
        if form.is_valid():
            a = request.POST['slot']
            a = Slot.objects.get(slot_id = a)
            obj = Ticket.objects.all().filter(slot= a , slot_active=True)
            if obj.count() == 0:
                form.save()
                return redirect('/ticket') 
            else:
                return render(request,'ticket/new_ticket.html',{'form':form,'messages':f'{a} Slot is alredy booked please choose diffrent slot','Slot':ls,'yes':True})
    print('hi'*10)
    return render(request,'ticket/new_ticket.html',{'form':form,'Slot':ls,'yes':True})

@login_required(login_url='/login')
@admin_only
def createSlot(request):
    slot = SlotForm()
    if request.method == 'POST':
        slot  = SlotForm(request.POST)
        if slot.is_valid():
            get = str(request.POST['slot_name'])
            try:
                alredy = str(Slot.objects.get(slot_name =get))
            except:
                alredy = ''
            if alredy != get:
                slot.save()
                return redirect('/ticket') 
            else:
                return render(request,'ticket/new_slot.html',{'slot':slot,'messages':f'{get} Slot name is alredy Present please choose diffrent name'})
    
    return render(request,'ticket/new_slot.html',{'slot':slot})
