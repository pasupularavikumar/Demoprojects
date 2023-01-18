from django.contrib import admin
from django.shortcuts import render
from .models import *



class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('created_by',)
    list_display = ('id','name','created_by',)

    def save_model(self, request, obj, form, change):
        if obj.id == None:
           obj.created_by = request.user
           super().save_model(request, obj, form, change)
        else:
           super().save_model(request, obj, form, change)


admin.site.register(Book, BookAdmin)
#admin.site.register(Book)