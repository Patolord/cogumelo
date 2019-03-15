from django.contrib import admin

from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','subject','contact_date')
    list_display_links = ('id','name')
    search_fields = ('name','email','subject','summary')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)