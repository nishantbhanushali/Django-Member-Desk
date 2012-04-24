from django.db import models

class Website(models.Model):
    name = models.CharField(max_length=128)
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
    domain = models.CharField(max_length=255)
    subdomain = models.CharField(max_length=255)
    
class Level(models.Model):
	website = models.ForeignKey(Website)
    name = models.CharField(max_length=128)
    number = models.IntegerField()