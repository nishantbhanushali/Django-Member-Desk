from django.db import models
import django_tables2 as tables
from django_tables2 import SingleTableView

class Member(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    
class MemberTable(tables.Table):
    class Meta:
        model = Member
        
class MemberList(SingleTableView):
    model = Member
    table_class = MemberTable