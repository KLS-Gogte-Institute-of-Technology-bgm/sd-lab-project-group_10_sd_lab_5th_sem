from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class  Profile(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    phone = models.CharField(max_length=12,null=True,default='')
    profile_pic = models.ImageField(default='profile.nef',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.user)
