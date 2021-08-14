from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.utils.avatar import compress_user_avatar


class User(AbstractUser):
    """Абстрактный пользователь"""

    nickname = models.CharField(_('Псевдоним'), max_length=50)
    avatar = models.ImageField(_("Аватарка пользователя"), blank=True, null=True)
    email = models.EmailField(_('Электронная почта'), unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.avatar:
            compress_user_avatar(self)
        super(User, self).save(*args, **kwargs)
