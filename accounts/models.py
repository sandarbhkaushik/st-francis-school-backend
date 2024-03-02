from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from allauth.account.signals import user_signed_up


class Profile(models.Model):
    user = models.OneToOneField(User,
                                primary_key=True,
                                verbose_name='user',
                                related_name='profile',
                                on_delete=models.CASCADE)
    avatar_url = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.user.email


@receiver(user_signed_up)
def save_profile(sociallogin, user, **kwargs):
    if sociallogin:
        if sociallogin.account.provider == 'google':
            picture_url = sociallogin.account.extra_data['picture']
    profile = Profile(user=user, avatar_url=picture_url)
    profile.save()
