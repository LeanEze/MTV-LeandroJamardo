from django.shortcuts import render
from django.http import HttpResponse

def datos_familiares(request):
    context = {}
    context["familiares"] = Familiar.objects.all()#modelo
    return render(request, "mi_app/datos_familiares.html", context)#templete
