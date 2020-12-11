from ticket.views import ticket
from django.shortcuts import render
from django.http import HttpResponse
from ticket.models import Ticket
from searchvehicle.filter import TicketFilter
from django.contrib.auth.decorators import login_required
from basic.decorators import allowed_users
# Create your views here.


@login_required(login_url='/login')
@allowed_users(allowed_roles=['manager','watchman'])
def search_vehicle(request):
    ticket = Ticket.objects.all()
    myFilter = TicketFilter(request.GET,queryset=ticket)
    ticket = myFilter.qs
    return render(request,'searchvehicle/search_vehicle.html',{'myFilter':myFilter,'ticket':ticket})
