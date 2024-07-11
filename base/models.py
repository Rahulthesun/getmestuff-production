from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class CreatorGoal(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.SET_NULL , null=True)
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



#Migration Model for Old user data

from django.db import models

class OldUser(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'auth_user'
        managed = False

    def __str__(self):
        return self.username



