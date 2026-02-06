from django.conf import settings
from django.db import models


class Address(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='addresses'
    )

    street = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=20)
    complement = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.street}, {self.number} - {self.city}/{self.state}'
