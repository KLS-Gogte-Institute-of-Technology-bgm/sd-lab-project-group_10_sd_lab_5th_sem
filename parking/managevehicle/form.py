from django.forms import ModelForm
from django.forms import fields
from ticket.models import Ticket

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
 