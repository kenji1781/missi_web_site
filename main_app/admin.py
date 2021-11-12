from django.contrib import admin
from .models import Machine_data,Machine_setting,Machine_drive_data

admin.site.register(Machine_data)
admin.site.register(Machine_setting)
admin.site.register(Machine_drive_data)

# Register your models here.
