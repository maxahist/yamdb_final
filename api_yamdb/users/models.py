from django.contrib.auth.models import (
    AbstractUser,
    UserManager,
)
from django.db import models

from core.constants import (
    ADMIN,
    MODERATOR,
    REG_USER
)
from .constants import (
    CHARS_FOR_CODE,
    CHARS_FOR_EMAIL,
    CHARS_FOR_PASSWORD,
    CHARS_FOR_ROLE,
)


class CustomUserManager(UserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('role', ADMIN)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (ADMIN, 'Admin'),
        (MODERATOR, 'Moderator'),
        (REG_USER, 'User')
    )
    role = models.CharField(choices=USER_TYPE_CHOICES,
                            max_length=CHARS_FOR_ROLE,
                            default=REG_USER,
                            verbose_name='статус')
    bio = models.TextField(blank=True,
                           null=True,
                           verbose_name='Биография')
    email = models.EmailField(max_length=CHARS_FOR_EMAIL,
                              blank=False,
                              null=False,
                              unique=True,
                              verbose_name='Почта')
    password = models.CharField(
        max_length=CHARS_FOR_PASSWORD,
        blank=True,
        null=True,
        verbose_name='Пароль'
    )
    confirmation_code = models.CharField(
        max_length=CHARS_FOR_CODE,
        blank=True,
        null=True,
        verbose_name='Код подтврждения'
    )
    objects = CustomUserManager()

    @property
    def is_admin(self):
        return self.role == ADMIN

    @property
    def is_moderator(self):
        return self.role == MODERATOR
