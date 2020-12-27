from django.forms import ModelForm, fields
from ticket.models import Slot

class SlotForm(ModelForm):
    class Meta:
        model = Slot
        fields = '__all__'