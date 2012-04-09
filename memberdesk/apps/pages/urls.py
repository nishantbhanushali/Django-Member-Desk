from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from pages.models import Page, PageTable
from django_tables2 import SingleTableView

urlpatterns = patterns("",
    url(r'^$', SingleTableView.as_view(model=Page,table_class=PageTable,template_name="pages/index.html")),
    url(r'^create/$', CreateView.as_view(model=Page)),
    url(r'^(?P<pk>\d+)/$', UpdateView.as_view(model=Page)),

)
