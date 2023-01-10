from django.contrib import admin
from .models import Employee,Score

# Register your models here.
class emplyeAdmin(admin.ModelAdmin):
    list_display=['firstName','lastName','salary','email']
admin.site.register(Employee,emplyeAdmin)
admin.site.register(Score)