from django.contrib import admin
# llamar al modelo Project
from .models import Project

# Clase para extender las funcionalidades del panel de admin.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    
    
# Resgistrar el modelo.
admin.site.register(Project, ProjectAdmin)