# Generated by Django 4.2.13 on 2024-07-03 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_creatorgoal_funded_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatorgoal',
            name='supporters',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]