from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'principal.views.index'),
    url(r'^inicio/$', 'principal.views.inicio'),
    url(r'^agregar_cxp/$', 'principal.views.agregar_cuenta'),
    url(r'^salir/$', 'principal.views.cerrar_sesion'),
    url(r'^editar_cxp/(?P<cuenta_id>\d+)$', 'principal.views.editar_cuenta'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
