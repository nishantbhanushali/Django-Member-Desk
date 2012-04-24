from django.db import models
from django.conf import settings

class WebsiteSpecificManager(models.Manager):
    def get_query_set(self):
        return super(WebsiteSpecificManager, self).get_query_set().filter(website=settings.website)