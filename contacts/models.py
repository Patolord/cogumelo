from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=55)
    subject = models.CharField(max_length=65, blank=True)
    message = models.TextField()
    contact_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name