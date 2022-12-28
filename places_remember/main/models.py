from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Post(models.Model):
    #basic data
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=410)

    #GEO data
    latitude = models.DecimalField(decimal_places=15, max_digits=18)
    longitude = models.DecimalField(decimal_places=15, max_digits=18)

    #author
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UserProfile(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_avatar_profile")
    imageUrl = models.CharField(max_length=150)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()