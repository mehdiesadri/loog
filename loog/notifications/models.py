from django.db import models

from core.tasks import send_email, send_web_push_notification, send_in_app_notification
from core.models import DateTimeModel
from accounts.models import User


class Notification(DateTimeModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    title = models.CharField(max_length=256)
    body = models.CharField(max_length=2048)
    icon_url = models.CharField(max_length=512, blank=True, null=True)
    url = models.CharField(max_length=512, blank=True, null=True)

    is_email = models.BooleanField(default=False)
    is_webpush = models.BooleanField(default=False)
    is_internal = models.BooleanField(default=False)

    def get_payload(self):
        return {
                'head': self.title,
                'body': self.body,
                'icon': self.icon_url,
                'url': self.url
            }
    
    def send_as_email(self):
        send_email.delay(
                subject=self.title,
                message=self.body,
                receivers=[self.user.email,]
            )
    
    def send_as_webpush(self):
        send_web_push_notification.delay(
                user_id=self.user.id,
                payload=self.get_payload(),
                ttl=1500
            )
    
    def send_as_internal(self):
        send_in_app_notification.delay(
                user_id=self.user.id,
                payload=self.get_payload()
            )

    def __str__(self) -> str:
        return str(self.title)