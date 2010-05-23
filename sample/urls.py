from django.conf.urls.defaults import *
from django.contrib import admin

from pdf import urls as pdf_urls


admin.autodiscover()

urlpatterns = patterns('',
    (r'^docs/', include(pdf_urls)),
    
    # Default login url
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
