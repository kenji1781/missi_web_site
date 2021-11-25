from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    class Meta:
        verbose_name_plural = '登録アカウント'

# Create your models here.
