from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Attendance(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="Attendances", on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)