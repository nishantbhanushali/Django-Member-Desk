from django.db import models
import django_tables2 as tables
from django_tables2 import SingleTableView
from django_tables2.utils import A
from products.models import Product
from members.models import Member

class Sale(models.Model):
	product = models.ForeignKey(Product)
	member = models.ForeignKey(Member)
	affiliate = models.ForeignKey(Member)
	transaction = models.CharField(max_length=128)
	subscription = models.CharField(max_length=128)
	transaction_type = models.CharField(max_length=128)
	customer_name = models.CharField(max_length=128)
	customer_email = models.EmailField()
	amount = models.CharField(max_length=128)
	#timestamp = models.CharField(max_length=128)
	
class AffiliateSale(models.Model):
	product = models.ForeignKey(Product)
	affiliate = models.ForeignKey(Member)
	sales_referred = models.IntegerField()
	sales_recieved = models.IntegerField()	
    
class SaleTable(tables.Table):
    edit = tables.TemplateColumn('<a class="btn" href="/sales/1">View</a>')
    class Meta:
        model = Sale
        attrs = {'class': 'table table-striped'}