from django.conf.urls import url
from django.contrib import admin

from recetas_app.views import home_views, user_views

urlpatterns = [
    url(r'^$', home_views.home, name='home'),
    url(r'^contacto$', home_views.contacto, name='contacto'),
    url(r'^registro$', user_views.registro, name='registro'),
    url(r'^admin/', admin.site.urls),
]
