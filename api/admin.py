from django.contrib import admin
from .models import Bills, Tax, Team

# Register your models here.
class BillsAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount')
    search_fields = ('title', 'amount')

admin.site.register(Bills, BillsAdmin)


class TaxAdmin(admin.ModelAdmin):
        list_display = ('title', 'amount')
        search_fields = ('title', 'amount')

admin.site.register(Tax, TaxAdmin)        


class TeamAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','title')
    search_fields = ('first_name', 'last_name', 'title')

admin.site.register(Team, TeamAdmin)    




