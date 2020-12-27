from ticket.views import ticket
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from ticket.models import Ticket
from django.contrib.auth.decorators import login_required
from basic.decorators import allowed_users
# Create your views here.

@login_required(login_url='/login')
@allowed_users(allowed_roles=['manager','watchman'])
def timeup(request):
    import datetime
    from datetime import date,timedelta
    x =datetime.date.today()
    startdate = date.today()
    enddate = startdate + timedelta(days=1)
    ticket_active = Ticket.objects.filter(date__range=[startdate, enddate],slot_active=True)

    print('hi',x)
    return render(request,'timeup/timeup.html',{'ticket':ticket_active})
