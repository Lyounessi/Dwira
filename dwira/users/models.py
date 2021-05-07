from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    """
    User's profile model
    """
    sex = [
        ( 'Homme' , 'Homme'),
        ( 'Femme' , 'Femmes')
        ]


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=500, blank=True)
    countrie = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    sexe = models.CharField(max_length=30, blank=True, choices=sex)
    email = models.EmailField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()