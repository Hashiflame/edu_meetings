from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=120, unique=True)
    email = models.EmailField(null=True)
    password = models.TextField()
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'


class MentorProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='mentor',
    )


class StudentProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='student',
    )

    def __str__(self):
        return self.user.username