# Generated by Django 4.2.13 on 2024-07-03 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatorGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=200)),
                ('item_link', models.URLField(blank=True, null=True)),
                ('item_name', models.CharField(max_length=200)),
                ('item_image', models.ImageField(upload_to='item_images/')),
                ('item_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SupporterInteraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supporter_email', models.EmailField(max_length=254)),
                ('redirect_link', models.URLField(blank=True, null=True)),
                ('date_interacted', models.DateTimeField(auto_now=True)),
                ('goal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.creatorgoal')),
            ],
        ),
    ]