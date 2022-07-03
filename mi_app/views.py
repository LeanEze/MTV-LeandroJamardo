from django.shortcuts import render
from django.http import HttpResponse
from mi_app.models import Familiar

def datos_familiares(request):
    context = {}
    context["familiares"] = Familiar.objects.all()#modelo
    return render(request, "mi_app/index.html", context)#templete
