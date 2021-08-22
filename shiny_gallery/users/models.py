import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    @property
    def name(self):
        return self.get_full_name()

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
