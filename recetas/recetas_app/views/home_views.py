from django.shortcuts import render

from recetas_app.models.receta import Receta


def home(request):
    recetas= Receta.objects.all()
    contexto = {
        'recetas': recetas
    }
    return render(request, "home.html", contexto)


def contacto(request):
    contexto = {}
    return render(request, "contacto.html", contexto)