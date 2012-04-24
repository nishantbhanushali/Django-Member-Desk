from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from website.models import Website
from django_tables2 import SingleTableView

urlpatterns = patterns("",
#    url(r'^$', SingleTableView.as_view(model=Website,table_class=MemberTable,template_name="members/index.html")),
#    url(r'^create/$', CreateView.as_view(model=Member)),
    url(r'$', UpdateView.as_view(model=Website)),

#    url(r'^$', SingleTableView.as_view(model=Member,table_class=MemberTable,template_name="members/index.html")),


)
