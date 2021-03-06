# Generated by Django 3.2.3 on 2021-08-06 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0024_auto_20210806_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='Luxury_Category',
            field=models.CharField(choices=[('Luxury', 'Luxury'), ('Economy', 'Economy')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='area',
            field=models.CharField(choices=[('Canal Road', 'Canal Road'), ('Central Park', 'Central Park'), ('Cantt', 'Cantt'), ('Johar Town', 'Johar Town'), ('Sadar', 'Sadar'), ('Askari', 'Askari'), ('Iqbal Town', 'Iqbal Town'), ('Gulberg', 'Gulberg'), ('Valencia Town', 'Valencia Town'), ('Ferozpur Road', 'Ferozpur Road'), ('Mall Road', 'Mall Road'), ('Ichra', 'Ichra'), ('DHA', 'DHA'), ('Lakshmi Chock', 'Lakshmi Chock'), ('Wapda Town', 'Wapda Town'), ('Township', 'Township'), ('Thokar', 'Thokar'), ('Jalo', 'Jalo'), ('Behria Town', 'Behria Town'), ('Model Town', 'Model Town')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Boys', 'Boys'), ('Both', 'Both'), ('Girls', 'Girls')], max_length=100),
        ),
    ]
