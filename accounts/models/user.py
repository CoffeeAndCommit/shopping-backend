from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)

    # Profile

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    # photo = models.ImageField(upload_to="users/photos/", blank=True, null=True)

    # Status flags
    is_verified = models.BooleanField(default=False)
    is_first_login = models.BooleanField(default=True)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-date_joined"]
        db_table = "users"



