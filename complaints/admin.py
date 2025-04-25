from django.contrib import admin
from .models import Project, Comment

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'identification_no', 'started_date', 'deadline_date', 'created_by')
    search_fields = ('project_name', 'identification_no')
    list_filter = ('started_date', 'deadline_date', 'created_by')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('project', 'text', 'created_by', 'created_at')
    search_fields = ('text', 'created_by__username')
    list_filter = ('created_at', 'created_by')
 
