from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    annotation = models.TextField(null=True, blank=True)
