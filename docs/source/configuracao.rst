Configuração
============

Após efetuar a instalação, vamos configurá-lo ao nosso projeto. Para isso, abra o arquivo ``settings.py`` e o adicione no ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        'contato',
    )

Não esquecendo que para enviar e-mails com Django, é necessário definir o servidor SMTP. Abaixo está conforme deve ser configurado, substituindo 
os valores do exemplo abaixo, com as informações pertinentes ao envio das mensagens::

    DEFAULT_FROM_EMAIL = 'contato@gilsondev.com'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'contato@gilsondev.com'
    EMAIL_HOST_PASSWORD = 'senha123456'
    EMAIL_USE_TLS = True    # Necessário para emails do tipo Gmail


Não é obrigatório, mas caso queira definir um prefixo no assunto das mensagens, faça conforme o exemplo abaixo::

    EMAIL_SUBJECT_PREFIX = u'[Nome do Seu Site]'


Agora vamos mapear as URLs da aplicação no arquivo ``urls.py``::

    urlpatterns = patterns('',
        # Examples:
        # url(r'^$', 'example.views.home', name='home'),
        # url(r'^example/', include('example.foo.urls')),

        # Uncomment the admin/doc line below to enable admin documentation:
        # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

        # Uncomment the next line to enable the admin:
        # url(r'^admin/', include(admin.site.urls)),

        url(r'', include('contato.urls')),
    )