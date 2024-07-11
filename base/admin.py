from django.contrib import admin
from .models import CreatorGoal , SupporterInteraction , OldUser

# Register your models here.

admin.site.register(CreatorGoal)
admin.site.register(SupporterInteraction)

admin.site.register(OldUser)
