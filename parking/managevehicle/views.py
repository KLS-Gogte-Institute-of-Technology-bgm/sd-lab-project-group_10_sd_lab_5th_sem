from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from ticket.models import Ticket,Slot
from .form import TicketForm
from django.contrib.auth.decorators import login_required
from basic.decorators import allowed_users
# Create your views here.

@login_required(login_url='/login')
@allowed_users(allowed_roles=['manager','watchman'])
def manage_vehicle(request):
    ticket_active = Ticket.objects.filter(slot_active = True)
    ticket_notactive = Ticket.objects.filter(slot_active = False)
    context = {'active':ticket_active,'notactive':ticket_notactive}
    return render(request,'managevehicle/manage_vehicle.html',context)

@login_required(login_url='/login')
@allowed_users(allowed_roles=['manager','watchman','customer'])
def updateTicket(request,pk):
    ticket = Ticket.objects.get(ticket_id=pk)
    form = TicketForm(instance=ticket)
    slot_left = Slot.objects.all()
    slot_left_extra = ticket.slot
    slot_reght = Ticket.objects.all().filter(slot_active=True)
    ls = []
    for i in slot_left:
        a = str(i)
        ls.append(a)
    ls.append(str(slot_left_extra))
    for j in slot_reght:
        b = str(j)
        try:
            ls.remove(b)
        except:
            pass
    if request.method == 'POST':
        check = request.POST['slot']
        check  = str(Slot.objects.get(slot_id=check))
        form = TicketForm(request.POST,instance=ticket)
        if check in ls:
            try:
                if form.is_valid():
                    form.save()
                    return redirect('/managevehicle')
                else:
                    return render(request,'managevehicle/update_ticket.html',{'form':form,'message':'Some details cant be cjamged '})
            except:
                return render(request,'managevehicle/update_ticket.html',{'form':form,'message':'Some details cant be changed '})
        else:
            return render(request,'managevehicle/update_ticket.html',{'form':form,'choice':ls,'message':'please select the slot which are available'})
    return render(request,'managevehicle/update_ticket.html',{'form':form,'choice':ls})
 