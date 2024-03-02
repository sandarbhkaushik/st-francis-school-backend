from django.db import models
import uuid
import os
import base64
from django.conf import settings
from menu_group.models import MenuItem
from slugify import slugify

def get_file_path(instance, filename):
    # filename = "%s.%s" % (uuid.uuid4(), filename)
    filename = "%s.%s" % (uuid.uuid4(), filename)
    return os.path.join(settings.MEDIA_ROOT, filename)

class CorePage(models.Model):
    slug = models.SlugField(unique=True)
    group_id = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, blank=True)
    content = models.TextField(
            db_column='data',
            blank=True)
    def save(self, *args, **kwargs):
        id = uuid.uuid4()
        self.slug = slugify(self.title + str(id))
        super(CorePage, self).save(*args, **kwargs)

    def set_data(self, data):
        self._data = base64.encodestring(data)

    def get_data(self):
        return base64.decodestring(self._data)

    data = property(get_data, set_data)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "WebPage"

class Media(models.Model):
    core_page_id = models.ForeignKey(CorePage, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=2500, blank=True)
    media_file = models.FileField(upload_to=get_file_path,blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Media"


class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,  null=True)
    media_file = models.ImageField(upload_to=get_file_path,blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    content = models.TextField(
            db_column='data',
            blank=True)
    
    def save(self, *args, **kwargs):
        id = uuid.uuid4()
        self.slug = slugify(self.title + str(id))
        super(Event, self).save(*args, **kwargs)

    def set_data(self, data):
        self._data = base64.encodestring(data)

    def get_data(self):
        return base64.decodestring(self._data)

    data = property(get_data, set_data)

    def __str__(self):
        return self.title

    
    class Meta:
        verbose_name_plural = "Event"

