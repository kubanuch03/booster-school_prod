from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.core.validators import RegexValidator

from .managers import UserManager



class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)

    phone_number = models.CharField(
        max_length=13,
        validators=[RegexValidator(r"^\+996\d{9}$")],
        blank=True,
        null=True,
    )
    token_auth = models.CharField(max_length=64, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.username}"
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        indexes = [
            models.Index(fields=['id']), 
            models.Index(fields=['email']), 
            models.Index(fields=['username']), 
        ]

