# Generated by Django 3.2.4 on 2021-08-07 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discovery', '0003_remove_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='Birthdate'),
        ),
        migrations.AddField(
            model_name='profile',
            name='preferences',
            field=models.IntegerField(choices=[(1, 'Ask me as many as there'), (2, 'All but very picky'), (3, 'Once a day'), (4, 'Mornings only'), (5, 'Around noon only'), (6, 'Late night only'), (7, 'Weekends only'), (8, 'Once a week')], default=1, verbose_name='User Preferences'),
        ),
    ]
