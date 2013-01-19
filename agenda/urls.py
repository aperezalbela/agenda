from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'agenda.views.home', name='home'),
    # url(r'^agenda/', include('agenda.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^listar-contactos/', 'contactos.views.lista_contactos'),
    url(r'^contacto/(?P<nombre_contacto>\w+)+$', 'contactos.views.detalle_contacto'),
)
