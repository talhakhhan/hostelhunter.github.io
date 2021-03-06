# Generated by Django 3.2.3 on 2021-08-08 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0032_auto_20210809_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='area',
            field=models.CharField(choices=[('Township', 'Township'), ('Ichra', 'Ichra'), ('Iqbal Town', 'Iqbal Town'), ('Askari', 'Askari'), ('Model Town', 'Model Town'), ('Thokar', 'Thokar'), ('DHA', 'DHA'), ('Ferozpur Road', 'Ferozpur Road'), ('Behria Town', 'Behria Town'), ('Central Park', 'Central Park'), ('Valencia Town', 'Valencia Town'), ('Canal Road', 'Canal Road'), ('Johar Town', 'Johar Town'), ('Sadar', 'Sadar'), ('Lakshmi Chock', 'Lakshmi Chock'), ('Mall Road', 'Mall Road'), ('Gulberg', 'Gulberg'), ('Jalo', 'Jalo'), ('Wapda Town', 'Wapda Town')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='standard',
            field=models.CharField(choices=[('Diamond', 'Diamond'), ('Gold', 'Gold'), ('Silver', 'Silver')], max_length=100),
        ),
    ]
