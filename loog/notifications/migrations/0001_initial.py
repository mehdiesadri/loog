# Generated by Django 3.2.4 on 2021-09-01 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('read', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=256)),
                ('body', models.CharField(max_length=2048)),
                ('icon_url', models.CharField(blank=True, max_length=512, null=True)),
                ('url', models.CharField(blank=True, max_length=512, null=True)),
                ('is_email', models.BooleanField(default=False)),
                ('is_webpush', models.BooleanField(default=False)),
                ('is_internal', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
