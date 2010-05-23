from django.conf.urls.defaults import patterns, url

from pdf.views import doc_detail
from pdf.views import doc_list
from pdf.views import doc_upload


urlpatterns = patterns('',
    url(r'^$', doc_list, name='pdf_list'),
    url(r'^upload/$', doc_upload, name='pdf_upload'),
    url(r'^(?P<uuid>[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})/$', doc_detail, name='pdf_detail'),
)
