from __future__ import unicode_literals

from base.models import TimeStampedModel
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserStatus(TimeStampedModel):
    """
    Model representing the status of a user being invited by
    other user to host/participate in a competition
    .. note::
        There are four different status:
            - Unknown.
            - Denied.
            - Accepted
            - Pending.
    """

    UNKNOWN = "unknown"
    DENIED = "denied"
    ACCEPTED = "accepted"
    PENDING = "pending"
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "accounts"


class Profile(TimeStampedModel):
    """
    Model to store profile of a user
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=10, blank=False, null=True)
    affiliation = models.CharField(max_length=512)
    receive_participated_challenge_updates = models.BooleanField(default=False)
    recieve_newsletter = models.BooleanField(default=False)
    github_url = models.URLField(max_length=200, null=True, blank=True)
    google_scholar_url = models.URLField(max_length=200, null=True, blank=True)
    linkedin_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.user)

    class Meta:
        app_label = "accounts"
        db_table = "user_profile"


class JwtToken(TimeStampedModel):
    """
    Model to store jwt tokens of a user
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=512, blank=False, null=True)
    refresh_token = models.CharField(max_length=512, blank=False, null=True)

    def __str__(self):
        return "{}".format(self.user)

    class Meta:
        app_label = "accounts"
        db_table = "jwt_token"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
