from django.db import models
from website.models import Website, Level
    
class Layout(models.Model):
    website = models.ForeignKey(Website)
    name = models.CharField(max_length=128)
    html = models.TextField()
    type = models.CharField(max_length=128)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    
class Page(models.Model):
    website = models.ForeignKey(Website)
    name = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    html = models.TextField()
    affiliate_visible = models.BooleanField()
    members_only = models.BooleanField()
    no_delete = models.BooleanField()
    show_in_navigation = models.BooleanField()
    level = models.ForeignKey(Level)
    layout = models.ForeignKey(Layout)
    order = models.IntegerField()
    days_required = models.IntegerField()
    date_required = models.DateTimeField()
    created = models.DateTimeField()
    modified = models.DateTimeField()