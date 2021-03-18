from django.db import models
# Create your models here.
class Customer(models.Model):
    name= models.CharField(max_length=25)
    email=models.EmailField()
    currentbal=models.IntegerField()
    
class Transfer(models.Model):
    sender=models.CharField(max_length=25)
    receiver=models.CharField(max_length=25)
    amount=models.IntegerField()
    transfertime=models.DateTimeField()    

