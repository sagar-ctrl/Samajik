from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from social.models import Profile


@receiver(post_save,sender=User)
def save_profile(sender,instance,created,**kw):
    if created:
        Profile.objects.create(user=instance,name=instance.username)