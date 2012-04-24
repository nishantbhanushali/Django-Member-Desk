from django.db import models

class Website(models.Model):
    name = models.CharField(max_length=128)
    domain = models.CharField(max_length=255)
    subdomain = models.CharField(max_length=255)    
    title = models.CharField(max_length=128)
    support_email = models.CharField(max_length=128)
    support_link = models.CharField(max_length=128)
    jv_password = models.CharField(max_length=128)
    cb_username = models.CharField(max_length=128)
    cb_secret = models.CharField(max_length=128)
    paypal_email = models.CharField(max_length=128)
    processor = models.IntegerField()
    theme = models.IntegerField()
    aweber_list = models.CharField(max_length=128)

class URL(models.Model):
    website = models.ForeignKey(Website)
    full_url = models.CharField(max_length=255)
    
    def get_site(request):
        host = request.get_host().lower()
        return URL.objects.filter(full_url=host).website
    
class Level(models.Model):
    website = models.ForeignKey(Website)
    name = models.CharField(max_length=128)
    number = models.IntegerField()