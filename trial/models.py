from django.db import models

# Create your models here.


class Info(models.Model):
    name = "Harith"
    age = 23

    def __str__(self) -> str:
        return self.name
