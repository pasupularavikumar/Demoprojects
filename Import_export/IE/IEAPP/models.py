from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Zone(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class School(models.Model):  
    state = models.ForeignKey(State, on_delete=models.CASCADE,   null=True,blank=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE,   null=True,blank=True)
    school_name = models.CharField(max_length=100,null=True,blank=True)
    phone_number = models.CharField(max_length=12,blank=True,null=True)
    address  = models.CharField(max_length=400,blank=True,null=True)

    def __str__(self):
        return self.school_name

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UpperModel(MyModel):
    class Meta:
        proxy = True

    def __str__(self):
        return self.name.upper()