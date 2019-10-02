from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Feedback(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
