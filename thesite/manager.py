from django.db import models

class WebsiteSpecificManager(models.Manager):
    def get_query_set(self):
        return super(WebsiteSpecificManager, self).get_query_set().filter(website=request.website)