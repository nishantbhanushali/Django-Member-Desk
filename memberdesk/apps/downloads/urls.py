from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from downloads.models import Download, DownloadTable
from django_tables2 import SingleTableView

urlpatterns = patterns("",
    url(r'^$', SingleTableView.as_view(model=Download,table_class=DownloadTable,template_name="downloads/index.html")),
    url(r'^create/$', CreateView.as_view(model=Download)),
    url(r'^(?P<pk>\d+)/$', UpdateView.as_view(model=Download)),

)
