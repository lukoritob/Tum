from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import default
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    address = models.IntegerField(default=0)
    mail = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=100, default='')

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
        
post_save.connect(create_profile, sender=User)

class VendorsTable(models.Model):
    Tender_Id = models.AutoField(primary_key=True)
    Project_Name = models.CharField(max_length=50)
    Bid_Amount_Ksh = models.IntegerField()
    Name = models.CharField(max_length=20)
    Address = models.CharField(max_length=20)
    Status = models.CharField(max_length=20)
    Accept = models.CharField(max_length=20)
    Reject = models.CharField(max_length=20)
    
class UpcomingTenders(models.Model):
    Tender_Id = models.AutoField(primary_key=True)
    Vendors_Name = models.CharField(max_length=20)
    Project_Name = models.CharField(max_length=20)
    Project_Type = models.CharField(max_length=50)
    Basic_Amount_Ksh = models.IntegerField()
    Bid_Close_Date = models.DateTimeField('date closed')
    Tender_Type = models.CharField(max_length=20)
    Project_file = models.CharField(max_length=20)
    Bid = models.CharField(max_length=20)
    
class BiddingStatusTable(models.Model):
    Tender_Id = models.AutoField(primary_key=True)
    Project_Name = models.CharField(max_length=20)
    Bid_Amount_Ksh = models.IntegerField()
    Name = models.CharField(max_length=20)
    Status = models.CharField(max_length=20)
    vendorstable = models.ManyToManyField(VendorsTable)
    
class ContactTable(models.Model):
    Number = models.AutoField(primary_key=True)
    Vendor_Name = models.CharField(max_length=20)
    upcomingtenders = models.ForeignKey(UpcomingTenders, on_delete=models.CASCADE)
    Mobile_No = models.IntegerField()
    Mail_Id = models.CharField(max_length=20)
    Address = models.IntegerField()
    
class BiddingTable(models.Model):
    Tender_Id = models.AutoField(primary_key=True)
    Project_Name = models.CharField(max_length=20)
    Bid_Amount_Ksh = models.IntegerField()
    
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    upload_at = models.DateTimeField(auto_now_add=True)

