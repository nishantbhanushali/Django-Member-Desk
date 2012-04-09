from django.db import models
import django_tables2 as tables
from django_tables2 import SingleTableView
from django_tables2.utils import A

class Page(models.Model):
    name = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    html = models.TextField()
    affiliate_visible = models.BooleanField()
    members_only = models.BooleanField()
    no_delete = models.BooleanField()
    level = models.ForeignKey(Level)
    layout = models.ForeignKey(Layout)
    order = models.IntegerField()
    days_required = models.IntegerField()
    date_required = models.DateTimeField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    
class Layout(models.Model):
    name = models.CharField(max_length=128)
    html = models.TextField()
    type = models.CharField(max_length=128)
    
class PageTable(tables.Table):
    edit = tables.TemplateColumn('<a class="btn" href="/page/1">Edit</a>')
    class Meta:
        model = Page
        attrs = {'class': 'table table-striped'}