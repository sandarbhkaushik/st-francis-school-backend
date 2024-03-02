from django.db import models
import uuid
import os
from slugify import slugify


class MenuItem(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        id = uuid.uuid4()
        self.slug = slugify(self.title + str(id))
        super(MenuItem, self).save(*args, **kwargs)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Menu Item"