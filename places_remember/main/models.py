from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    # basic data
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=410)

    # GEO data
    latitude = models.DecimalField(decimal_places=15, max_digits=18)
    longitude = models.DecimalField(decimal_places=15, max_digits=18)

    # author
    user = models.ForeignKey(User, on_delete=models.CASCADE)
