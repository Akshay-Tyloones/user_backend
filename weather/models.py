from django.db import models
from django.contrib.auth.models import AbstractUser


class UserDetails(AbstractUser):
    cognito_user = models.CharField(default="hello", max_length=100)
    is_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=10, null=True)
    image_url = models.URLField(default=None, null=True)

    def __str__(self) -> str:
        return self
    
class Subscription(models.Model):
    username = models.CharField(max_length=50, null=True)
    event = models.CharField(max_length=100)
    connection_id = models.CharField(max_length=100)






