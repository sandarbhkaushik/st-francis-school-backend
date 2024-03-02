from django.db import models
import uuid
import os
import base64
from django.conf import settings

class Department(models.Model):
    slug = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2000, blank=True)

    def save(self, *args, **kwargs):
        id = uuid.uuid4()
        self.slug = slugify(self.title + str(id))
        super(MenuItem, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Departments"