# Generated by Django 2.1.1 on 2018-10-19 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0008_strategy_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='strategy',
            old_name='user_id',
            new_name='userid',
        ),
    ]