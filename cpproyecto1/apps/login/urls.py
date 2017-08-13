from django.conf.urls import url
#importamos las vistas de views login

from apps.login.views import index, loguear_view

urlpatterns = [
    url(r'^$', loguear_view, name='loguear_crear'),
    url(r'^login$', index, name='index'),
]

