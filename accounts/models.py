from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Override username usage
    username = None
    email = models.EmailField(unique=True)

    # Profile
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    photo = models.ImageField(upload_to="users/photos/", blank=True, null=True)

    # Status flags
    is_verified = models.BooleanField(default=False)
    is_first_login = models.BooleanField(default=True)
    is_blocked = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-date_joined"]
        db_table = "users"



class Address(models.Model):
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="addresses"
    )
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
