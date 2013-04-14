from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url')

admin.site.register(Project, ProjectAdmin)
