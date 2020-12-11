from django.db import models

# Create your models here.

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50,null=True)
    describe = models.CharField(max_length=200,default='',null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.type