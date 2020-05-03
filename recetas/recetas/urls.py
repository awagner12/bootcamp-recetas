from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from recetas_app.views import home_views, user_views, recetas_view

urlpatterns = [
      url(r'^$', home_views.home, name='home'),
      url(r'^contacto$', home_views.contacto, name='contacto'),
      url(r'^registro$', user_views.registro, name='registro'),
      url(r'^login$', user_views.login, name='login'),
      url(r'^logout$', user_views.logout, name='logout'),
      url(r'^admin/', admin.site.urls),

      path('receta/<slug:slug>/', recetas_view.receta, name='receta'),

  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
