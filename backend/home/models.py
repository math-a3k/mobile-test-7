from django.conf import settings
from django.db import models


class Pet(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
