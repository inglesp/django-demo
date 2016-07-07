from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()

    class Meta:
        verbose_name_plural = 'people'

    def __str__(self):
        return self.name
