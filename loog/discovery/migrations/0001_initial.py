# Generated by Django 3.2.4 on 2021-08-07 07:23

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
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('value', models.IntegerField(default=-1, verbose_name='Value')),
            ],
        ),
        migrations.CreateModel(
            name='TagAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('giver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='receiver', to=settings.AUTH_USER_MODEL, verbose_name='Giver')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Receiver')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='discovery.tag', verbose_name='Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user_profiles/', verbose_name='Avatar')),
                ('bio', models.TextField(blank=True, max_length=256, null=True, verbose_name='Biography')),
                ('location', models.CharField(blank=True, max_length=64, null=True, verbose_name='Location')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='InvitedUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('is_registered', models.BooleanField(default=False, verbose_name='Registered')),
                ('comma_separated_tags', models.CharField(max_length=1024, verbose_name='Comma Separated Tags')),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Inviter')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
