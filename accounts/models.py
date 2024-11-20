from django.db import models
from django.contrib.auth.models import AbstractUser

# 扩展默认用户模型
class CustomerUser(AbstractUser):
  bio = models.TextField(blank=True, null=True)
  avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
  phone = models.CharField(max_length=15, blank=True, null=True)

  def __str__(self):
    return self.username
