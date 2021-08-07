# Generated by Django 3.2.6 on 2021-08-06 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discovery', '0012_alter_profile_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='value',
            field=models.IntegerField(default=-1, verbose_name='Value'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=32, verbose_name='Name'),
        ),
    ]