from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Invoice(models.Model):
    book=models.CharField(max_length=20,null=True,blank=True)
    quantity=models.CharField(max_length=10,null=True,blank=True)
    buyer=models.CharField(max_length=10,null=True,blank=True)
    dt=models.DateField(max_length=10,null=True,blank=True)
    dr=models.DateField(max_length=10,null=True,blank=True)
    user=models.ForeignKey(User,related_name="library1",on_delete=models.DO_NOTHING)
    #image=models.ImageField(null=True,blank=True,upload_to="images/")

def __str__(self):
    return self.title