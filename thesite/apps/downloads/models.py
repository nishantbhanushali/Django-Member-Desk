from django.db import models
from website.models import Level

class Download(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    filename = models.TextField()
    level = models.ForeignKey(Level)
    days_required = models.IntegerField()
    date_required = models.DateTimeField()

    created = models.DateTimeField()
    modified = models.DateTimeField()    