from django.db import models
from django.contrib.auth.models import User
from django.conf import settings




# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,editable=False)

    def _str__(self):
        return self.name