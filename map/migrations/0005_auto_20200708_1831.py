# Generated by Django 3.0.8 on 2020-07-08 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20200708_1829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='big',
            old_name='forget',
            new_name='memory',
        ),
        migrations.RenameField(
            model_name='middle',
            old_name='forget',
            new_name='memory',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='forget',
            new_name='memory',
        ),
    ]
