from django.contrib import admin

from ticket.models import Ticket,Slot
# Register your models here.

admin.site.register(Ticket)
admin.site.register(Slot)