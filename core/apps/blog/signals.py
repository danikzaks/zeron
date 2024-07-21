from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Post


@receiver(post_save, sender=Post)
def send_post_notification(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'New Post Created',
            f'A new post titled "{instance.title}" has been created.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )
