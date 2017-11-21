from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^grado/nuevo/$', views.grado_nuevo, name='grado_nuevo'),
    url(r'^grados/listagrados/$', views.listar, name='listar'),
    ]
