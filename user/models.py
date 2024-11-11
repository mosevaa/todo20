from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CharField,
    EmailField,
    DateTimeField
)

class User(AbstractUser):
    name = CharField(max_length=50, null=False)
    surname = CharField(max_length=50, null=False)
    second_name = CharField(max_length=50, null=True)
    email = EmailField(null=False, max_length=100)
    created_at = DateTimeField(null=False, auto_now_add=True)

    class Meta:
        ordering = ["surname"]
