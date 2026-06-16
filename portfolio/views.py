from django.shortcuts import render
from .models import Project
# Create your views here.
def portfolio (request):
    projects = Project.objects.all()
    # cadena=['PATRICIO ANDRES LEPPE ASTORGA EL GUAPO DE TODA LA NACIONNNNNNN']
    # lista = [1,2,3]
    return render(request, "portfolio/portfolio.html", {'projects': projects})