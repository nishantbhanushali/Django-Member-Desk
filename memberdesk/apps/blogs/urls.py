from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from blogs.models import Blog, BlogTable
from django_tables2 import SingleTableView

urlpatterns = patterns("",
    url(r'^$', SingleTableView.as_view(model=Blog,table_class=BlogTable,template_name="blogs/index.html")),
    url(r'^create/$', CreateView.as_view(model=Blog)),
    url(r'^(?P<pk>\d+)/$', UpdateView.as_view(model=Blog)),

)
