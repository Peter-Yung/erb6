from django.contrib import admin

# Register your models here.
from .models import Listing
from django.forms import NumberInput
from django.db import models

class ListingAdmin(admin.ModelAdmin):
    # All are python tuples! So no need to add any ()
    # This code define the listing table fields on backend for user to make changes of data from DB.
    list_display = 'id', 'title', 'is_published', 'price', 'list_date', 'realtor'
    list_display_links = 'id', 'title'
    # Add filter box on the right of listing table.
    list_filter = 'realtor',
    list_editable = 'is_published','price'
    # Define which data field could be search by the search box.
    search_fields = 'title','description','address','price'
    # Paganation of maximum records per pages.
    list_per_page = 25 
    # Follow codes is to extend length of all IntegerField (e.g.price field)
    ordering = ['-id']
    prepopulated_fields = {'title': ('title',)}
    formfield_overrides = {
        models.IntegerField: {'widget': NumberInput(attrs={'size' : '10'})}
    }
    # This code added listing items counts per realtors
    show_facets = admin.ShowFacets.ALWAYS

admin.site.register(Listing, ListingAdmin)
