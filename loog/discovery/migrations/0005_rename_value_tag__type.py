# Generated by Django 3.2.4 on 2021-08-08 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discovery', '0004_auto_20210807_2150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='value',
            new_name='_type',
        ),
    ]