from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

 
      
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True,default=None,)
    name = models.CharField(max_length=200, null=False, blank=False,unique = True)
    email = models.EmailField(max_length=100,blank=True, null=True,unique = True)
    phonenumber = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.name
    def create_user(self):
        if not self.user:
            user = User.objects.create(username=self.name,email=self.email,password=self.phonenumber)
            self.user= user
            self.save()