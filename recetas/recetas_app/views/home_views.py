from django.core.mail import send_mail
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
    if request.method == "POST":
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        # print ("{} {}".format(email, mensaje))
        mensaje_html = "email: {} <br/> mensaje: {}".format(email, mensaje)
        send_mail("Contacto de recetas",
                  mensaje_html,
                  'info@recetas.com',
                  ['destinatario@recetas.com'])
        contexto['mensaje'] = "Petición eviada correctamente"
    return render(request, "contacto.html", contexto)