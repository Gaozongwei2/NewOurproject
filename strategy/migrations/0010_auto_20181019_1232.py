# Generated by Django 2.1.1 on 2018-10-19 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_content'),
        ('strategy', '0009_auto_20181019_0957'),
    ]

    operations = [
        migrations.DeleteModel(
            name='test',
        ),
    ]
