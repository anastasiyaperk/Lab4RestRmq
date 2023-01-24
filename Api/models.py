from django.db import models


class CSV(models.Model):
    id = models.UUIDField(primary_key=True, unique=True)
    name = models.CharField(max_length=150)
    binary_data = models.BinaryField()
