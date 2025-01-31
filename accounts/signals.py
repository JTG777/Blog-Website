from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save,sender=User)
def create_profile_for_user(sender,instance,created,**kwargs):
    # creates a new profile for user
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_or_update_profile(sender,instance,**kwargs):
    # save or update profile

    instance.profile.save() 

    # reverse relationship , its similiar as writing profile=Profile.objects.get(user=instance) , profile.save()