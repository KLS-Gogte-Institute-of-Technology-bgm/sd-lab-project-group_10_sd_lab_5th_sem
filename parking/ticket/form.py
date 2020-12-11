from django.forms import ModelForm
from django.forms import fields
from .models import Ticket,Slot

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'

class SlotForm(ModelForm):
    class Meta:
        model = Slot
        fields = '__all__'