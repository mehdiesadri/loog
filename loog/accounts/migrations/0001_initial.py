# Generated by Django 3.2.4 on 2021-08-10 04:43

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user_profiles/', verbose_name='Avatar')),
                ('location', models.CharField(blank=True, max_length=64, null=True, verbose_name='Location')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='Birthdate')),
                ('preferences', models.IntegerField(choices=[(1, 'Ask me as many as there'), (2, 'All but very picky'), (3, 'Once a day'), (4, 'Mornings only'), (5, 'Around noon only'), (6, 'Late night only'), (7, 'Weekends only'), (8, 'Once a week')], default=1, verbose_name='User Preferences')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='InvitedUser',
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