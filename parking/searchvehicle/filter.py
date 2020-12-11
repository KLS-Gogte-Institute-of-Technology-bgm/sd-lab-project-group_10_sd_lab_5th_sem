import django_filters
from ticket.models import Ticket
from django_filters import DateFilter

class TicketFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date',lookup_expr='gte')
    end_date = DateFilter(field_name='date',lookup_expr='lte')
    class Meta :
        model = Ticket
        fields = ['vehicle_number','owner_name','phone_number','slot']
       