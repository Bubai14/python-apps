from django.contrib import admin

from .models import JobForm


# Customize the admin interface
class JobFormAdmin(admin.ModelAdmin):
    # Show the list of columns to the displayed in the admin screen
    list_display = ('first_name', 'last_name', 'email')
    # Add search fields
    search_fields = ('first_name', 'last_name', 'email')
    # Add filters
    list_filter = ('occupation', 'start_date')
    # order the list
    ordering = ('first_name',)
    # Make readonly fields
    readonly_fields = ('occupation',)


# Register your models here.
admin.site.register(JobForm, JobFormAdmin)
