# Generated by Django 3.2.6 on 2021-08-06 16:44

import discovery.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discovery', '0013_auto_20210806_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='invitation_code',
            field=models.CharField(default=discovery.models.get_invitation_code, editable=False, max_length=10, unique=True, verbose_name='Invitation Code'),
        ),
        migrations.CreateModel(
            name='InvitedUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invited_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]