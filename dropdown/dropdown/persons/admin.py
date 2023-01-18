from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([Country,City,Person])

admin.site.register([Demo1,Demo2,Info])
admin.site.register(school)