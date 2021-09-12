from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from .models import User
from .helper import send_invitation, encrypt_id


@receiver(post_save, sender=User)
def send_new_officer_notification_email(sender, instance, created, **kwargs):
    if created:
        send_invitation('Invitation Email', instance.email,
                        render_to_string('accounts/password/invitation_email.html', {'hash': encrypt_id(instance.id)}))
