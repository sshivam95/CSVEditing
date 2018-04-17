from django.db import models
from __future__ import unicode_literals

# Create your models here.
class Document(models.Model):
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
