from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Профиль пользователя',
        related_name='profile',
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения',
    )
    avatar = models.ImageField(
        upload_to='avatars',
        null=True,
        blank=True,
        verbose_name='Аватар'
    )
    github_profile = models.URLField(max_length=500, null=True, blank=True)
    about_me = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'profiles'
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
