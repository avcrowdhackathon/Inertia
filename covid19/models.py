import uuid

from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    height = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=4, decimal_places=2)


class Session(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    protocol = models.CharField(max_length=20, blank=True)
    tested_for = models.CharField(max_length=20, blank=True)
    recording = models.FileField(upload_to='sessions/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
