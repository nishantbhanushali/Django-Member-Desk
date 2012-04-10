from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from products.models import Product, ProductTable
from django_tables2 import SingleTableView

urlpatterns = patterns("",
    url(r'^$', SingleTableView.as_view(model=Product,table_class=ProductTable,template_name="products/index.html")),
    url(r'^create/$', CreateView.as_view(model=Product)),
    url(r'^(?P<pk>\d+)/$', UpdateView.as_view(model=Product)),

)
