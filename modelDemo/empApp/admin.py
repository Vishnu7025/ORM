from django.contrib import admin
from .models import Employee

# Register your models here.
class emplyeAdmin(admin.ModelAdmin):
    list_display=['firstName','salary','email']
admin.site.register(Employee,emplyeAdmin)