# Generated by Django 4.2.13 on 2024-07-07 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_supporterinteraction_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creatorgoal',
            name='supporters',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
