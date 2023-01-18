from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *

class SchoolAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(School, SchoolAdmin)  

class StateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...  

admin.site.register(State,StateAdmin)  
admin.site.register(Zone,StateAdmin)