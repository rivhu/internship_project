from django.contrib.auth.models import User
from django.db import models

class TelegramUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_username = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.telegram_username}"

# Create your models here.
