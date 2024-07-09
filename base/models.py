from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class CreatorGoal(models.Model):
    creator = models.ForeignKey(User , on_delete=models.SET_NULL , null=True)
    channel_name = models.CharField(max_length=200)
    item_link = models.URLField(max_length = 200 , null = True , blank = True)
    item_name = models.CharField(max_length=200)
    item_image = models.ImageField(upload_to='item_images/')
    item_price = models.DecimalField(default=0.00 , decimal_places=2 , max_digits=10)
    
    funded_amount = models.DecimalField(default=0.00 , decimal_places=2 , max_digits=10)
    funded_percent = models.DecimalField(default=0.00 , decimal_places=2 , max_digits=10)
    supporters = models.IntegerField(default = 0 , null=True , blank=True)

    date_created = models.DateTimeField(auto_now=True)

class SupporterInteraction(models.Model):
    goal = models.ForeignKey(CreatorGoal , on_delete=models.SET_NULL , null=True)
    donation_amount = models.DecimalField(default=0.00 , decimal_places=2 , max_digits=10)

    supporter_email = models.EmailField()
    redirect_link = models.URLField(max_length=200, null=True , blank=True)

    paid = models.BooleanField(default=False)
    date_interacted = models.DateTimeField(auto_now=True)



