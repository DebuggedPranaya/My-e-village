from django.contrib import admin
from application.models import *

# Register your models here.
admin.site.register(enquiryform)  

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display  = ['title', 'category', 'is_active', 'expiry_date']
    list_filter   = ['category', 'is_active']
    list_editable = ['is_active']

@admin.register(Festival)
class FestivalAdmin(admin.ModelAdmin):
    list_display = ['name', 'month', 'order']
    list_filter = ['month']
    list_editable = ['order']