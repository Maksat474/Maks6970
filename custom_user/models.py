from django.db import models
from django.contrib.auth.models import User

GENDER = (
    ('MALE', "MALE"),
    ('FEMALE', "FEMALE"),
    ('OTHER', "OTHER"),
)


class CustomUser(User):
    phone_number = models.CharField(max_length=30, default="+996")
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=100, choices=GENDER)
    address = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)

