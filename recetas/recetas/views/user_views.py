from django.shortcuts import render


def registro(request):
    contexto = {}
    return render(request, "usuario/registro.html", contexto)