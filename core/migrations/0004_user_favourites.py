# Generated by Django 3.2.3 on 2021-05-23 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favourites',
            field=models.CharField(default='', max_length=200),
        ),
    ]
