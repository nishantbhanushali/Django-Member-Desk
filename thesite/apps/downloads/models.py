from django.db import models
from website.models import Level, Website
from manager import WebsiteSpecificManager

class Download(models.Model):
    website = models.ForeignKey(Website)
    name = models.CharField(max_length=128)
    description = models.TextField()
    filename = models.TextField()
    level = models.ForeignKey(Level)
    days_required = models.IntegerField()
    date_required = models.DateTimeField()
    type = models.CharField(max_length=128)

    created = models.DateTimeField()
    modified = models.DateTimeField()
    
    objects = WebsiteSpecificManager()
    all_objects = models.Manager()
    
    @property
    def is_available(self):
        if date.today() > self.date_required:
            return True
        return False
