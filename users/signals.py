from users.models import CustomUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail


@receiver(post_save, sender=CustomUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            "Welcome to GoodReads Clone",
            f"Hi, {instance.username}. Welcome to GoodReads Clone. Enjoy the books and reviews",
            "doniyortursunvoyev@gmail.com",
            [instance.email]
        )
