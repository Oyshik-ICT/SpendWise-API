from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Catagoery(models.Model):
    groceries = models.FloatField(default=0)
    leisure = models.FloatField(default=0)
    electronics = models.FloatField(default=0)
    utilities = models.FloatField(default=0)
    clothing = models.FloatField(default=0)
    health = models.FloatField(default=0)
    others = models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
