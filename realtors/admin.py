from django.contrib import admin

from .models import Realtor
# Register your models here.
# Define a super class. 
# Before Django 5.2, lack of libraries so it use python declarator @xxxx statement to call function outside Django.

class RealtorAdmin(admin.ModelAdmin):
    # This code define the listing table fields on backend for user to make changes of data from DB.
    list_display = ('id','name','email','hire_date')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)
