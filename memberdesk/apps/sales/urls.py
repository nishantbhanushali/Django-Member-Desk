from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from sales.models import Sale, SaleTable
from django_tables2 import SingleTableView

urlpatterns = patterns("",
    url(r'^$', SingleTableView.as_view(model=Sale,table_class=SaleTable,template_name="sales/index.html")),
    url(r'^(?P<pk>\d+)/$', UpdateView.as_view(model=Sale)),

)
