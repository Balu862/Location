from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class PlacesModel(models.Model):

    user_name = models.ForeignKey(
        User, related_name="User_Name", on_delete=models.CASCADE
    )
    place_name = models.CharField(default="")
    description = models.TextField(default="")
    latitude = models.CharField(default="")
    longitude = models.CharField(default="")
    created_at = models.DateTimeField(auto_now=True)
