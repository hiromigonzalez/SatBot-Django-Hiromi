from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('student', 'Student'),
        ('professor', 'Professor'),
    )
    role = models.CharField(max_length=10, choices=USER_ROLES, default='student')
    user_id = models.BigAutoField(primary_key=True)  # Using BigAutoField for future-proofing

    def __str__(self):
        return self.username

