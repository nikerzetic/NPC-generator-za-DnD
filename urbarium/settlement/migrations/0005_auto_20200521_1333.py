# Generated by Django 3.0.4 on 2020-05-21 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settlement', '0004_auto_20200514_1347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settlement',
            old_name='know_for',
            new_name='knownfor',
        ),
    ]
