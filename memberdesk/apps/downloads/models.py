from django.db import models
import django_tables2 as tables
from django_tables2 import SingleTableView
from django_tables2.utils import A

class Download(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    filename = models.TextField()
    level = models.ForeignKey(Level)
    days_required = models.IntegerField()
    date_required = models.DateTimeField()

    created = models.DateTimeField()
    modified = models.DateTimeField()    
    
class DownloadTable(tables.Table):
    edit = tables.TemplateColumn('<a class="btn" href="/downloads/1">Edit</a>')
    class Meta:
        model = Download
        attrs = {'class': 'table table-striped'}