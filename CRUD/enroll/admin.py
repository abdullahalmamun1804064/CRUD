from django.contrib import admin

# Register your models here.
from . import models
class show(admin.ModelAdmin):
    list_display=('id','name','email','password')

admin.site.register(models.studentinfo,show)
