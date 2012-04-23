from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    html = models.TextField()
    affiliate_visible = models.BooleanField()
    members_only = models.BooleanField()
    no_delete = models.BooleanField()
    show_in_navigation = models.BooleanField()
    #level = models.ForeignKey(Level)
    #layout = models.ForeignKey(Layout)
    order = models.IntegerField()
    days_required = models.IntegerField()
    date_required = models.DateTimeField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    
class Layout(models.Model):
    name = models.CharField(max_length=128)
    html = models.TextField()
    type = models.CharField(max_length=128)
    created = models.DateTimeField()
    modified = models.DateTimeField()