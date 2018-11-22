from django.db import models

# Create your models here.
# 定义 User 类


class User(models.Model):
    username = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"
