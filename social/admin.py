from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from .models import Profile, MyPost


class ProfileAdmin(ModelAdmin):
    list_display = ['name']
    
    search_fields = ['name']


admin.site.register(Profile,ProfileAdmin)
admin.site.register(MyPost)
