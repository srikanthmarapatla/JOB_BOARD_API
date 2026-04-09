from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'category', 'status', 'salary', 'created_at')
    list_filter = ('status', 'category')
    search_fields = ('title', 'company__username')