from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from members.models import Member

urlpatterns = patterns("",
    url(r'^$', ListView.as_view(model=Member,template_name='members/index.html')),
    url(r'^create/$', CreateView.as_view(model=Member)),
    url(r'^(?P<pk>\d+)/$', UpdateView.as_view(model=Member)),

)
