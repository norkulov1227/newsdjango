# Generated by Django 5.0.6 on 2024-07-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='view',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]
