# Generated by Django 3.2.3 on 2021-05-23 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_alter_listing_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='no_of_rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='total_rating',
            field=models.IntegerField(null=True),
        ),
    ]
