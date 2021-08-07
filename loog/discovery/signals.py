import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, Profile, InvitedUser

logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        logging.warning("discovery.signals.create_user_profile: Profile does not exists.")
        Profile.objects.create(user=instance)


@receiver(post_save, sender=InvitedUser)
def invite_user(sender, instance, created, **kwargs):
    if created or not instance.is_registered:
        # TODO: Do this with Celery
        instance.send_invitation_email()
