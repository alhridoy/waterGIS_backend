from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    email = models.EmailField(
        max_length=150,
        unique=True,
        error_messages={
            "unique": "The email must be unique"
        }
    )
    groups = models.ManyToManyField(Group, related_name="custom_user_groups")
    user_permissions = models.ManyToManyField(
        Permission, related_name="custom_user_permissions")

    profile_image = models.ImageField(
        null=True,
        blank=True,
        upload_to="profile_images"
    )

    REQUIRED_FIELDS = ["email"]
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def get_profile_picture(self):
        url = ""
        try:
            url = self.profile_image.url
        except:
            url = ""
        return url


class UserProfile(models.Model):
    user = models.OneToOneField(User,  null=True, on_delete=models.SET_NULL)
    IS_PREMIUM_CHOICES = [
        ('NO', 'Not a premium user'),
        ('PENDING', 'Pending approval for premium access'),
        ('YES', 'Is a premium user'),
    ]
    is_premium_user = models.CharField(
        max_length=20,
        choices=IS_PREMIUM_CHOICES,
        default='NO',
    )
