from typing import Match
from django.db import models
from vehiclecategory.models import Category
# Create your models here.

class Slot(models.Model):
    slot_id = models.AutoField(primary_key=True)
    slot_name = models.CharField(max_length=50,null=True)
    describe = models.CharField(max_length=50,null=True,blank=True,default='')
    def __str__(self) :
        return self.slot_name

class Ticket(models.Model):
    VALID = (
        ('2 hours','2 hours'),
        ('4 hours','4 hours'),
        ('8 hours','8 hours'),
        ('12 hours','12 hours'),
        ('24 hours','24 hours')
    )
    ticket_id = models.AutoField(primary_key=True)
    vehicle_type = models.ForeignKey(Category,null=True, on_delete=models.SET_NULL)
    owner_name = models.CharField(max_length=200,null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)
    vehicle_number=models.CharField(null=True,max_length=6)
    phone_number=models.CharField(null=True,max_length=12,default='')
    slot = models.ForeignKey(Slot,null=True,on_delete=models.SET_NULL)
    slot_active = models.BooleanField(null=True,default=True)
    valid_time = models.CharField(null=True,blank=True,choices=VALID,max_length=20)
    def __str__(self):
        return str(self.slot)
