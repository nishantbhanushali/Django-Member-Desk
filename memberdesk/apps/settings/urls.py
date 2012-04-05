from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from members.models import Member, MemberTable
from django_tables2 import SingleTableView

urlpatterns = patterns("",
    url(r'^$', SingleTableView.as_view(model=Member,table_class=MemberTable,template_name="members/index.html")),
    url(r'^create/$', CreateView.as_view(model=Member)),
    url(r'^(?P<pk>\d+)/$', UpdateView.as_view(model=Member)),

)
