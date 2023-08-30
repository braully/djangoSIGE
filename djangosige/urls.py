# -*- coding: utf-8 -*-

from django.urls import re_path as url, include
from django.contrib import admin
from django.conf.urls.static import static
from .configs.settings import DEBUG, MEDIA_ROOT, MEDIA_URL

# admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('djangosige.apps.base.urls')),
    url(r'^login/', include('djangosige.apps.login.urls')),
    url(r'^cadastro/', include('djangosige.apps.cadastro.urls')),
    url(r'^fiscal/', include('djangosige.apps.fiscal.urls')),
    url(r'^vendas/', include('djangosige.apps.vendas.urls')),
    url(r'^compras/', include('djangosige.apps.compras.urls')),
    url(r'^financeiro/', include('djangosige.apps.financeiro.urls')),
    url(r'^estoque/', include('djangosige.apps.estoque.urls')),
    # novos
    url(r'^boletos/', include('djangosige.apps.boletos.urls')),
    url(r'^relatorios/', include('djangosige.apps.relatorios.urls')),

    url(r'^todo/', include('todo.urls', namespace="todo")),
]

if DEBUG is True:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
