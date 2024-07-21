from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from django.core.mail import send_mail
from .models import Post
import os

sitemap_update_signal = Signal()


@receiver(post_save, sender=Post)
def post_save_handler(sender, instance, created, **kwargs):
    if created:
        sitemap_update_signal.send(sender=sender, instance=instance)


@receiver(sitemap_update_signal)
def update_sitemap(sender, **kwargs):
    os.system("py manage.py refresh_sitemap")


@receiver(post_save, sender=Post)
def send_post_notification(sender, instance, created, **kwargs):
    if created:
        send_mail(
            "New Post Created",
            f'A new post titled "{instance.title}" has been created.',
            "from@example.com",
            ["to@example.com"],
            fail_silently=False,
        )
