from django.shortcuts import render
from django.http import HttpResponse
from ticket.models import Ticket 
from vehiclecategory.models import Category
from django.contrib.auth.decorators import login_required
from basic.decorators import allowed_users
# Create your views here.

@login_required(login_url='/login')
@allowed_users(allowed_roles=['manager','watchman'])
def analysis(request):
    import datetime
    veh = Category.objects.all()
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    try:
        four_today = len(Ticket.objects.filter(vehicle_type=veh[0],date__range=(today_min, today_max)))
        two_today = len(Ticket.objects.filter(vehicle_type = veh[1],date__range=(today_min, today_max)))
        bicy_today = len(Ticket.objects.filter(vehicle_type = veh[2],date__range=(today_min, today_max)))
    except:
        four_today = 0
        two_today = 0
        bicy_today = 0
    try:
        four_total = len(Ticket.objects.filter(vehicle_type=veh[0]))
        two_total = len(Ticket.objects.filter(vehicle_type = veh[1]))
        bicy_total = len(Ticket.objects.filter(vehicle_type = veh[2]))
    except:
        four_total = 0
        two_total = 0
        bicy_total = 0
    if len(veh)==0:
        veh = []
        veh.append('a')
        veh.append('b')
        veh.append('c')
    

    context = {
        'labels':[str(veh[0]),str(veh[1]),str(veh[2])],
        'data_today':[four_today,two_today,bicy_today],
        'data_total':[four_total,two_total,bicy_total],
        'four_today':[four_today],
        'two_today':[two_today],
        'bicy_today':[bicy_today],
        'a':[str(veh[0])],
        'b':[str(veh[1])],
        'c':[str(veh[2])]
        }
    return render(request,'analysis/analysis.html',context)