from django.db import models
import uuid
import os
import base64
from django.conf import settings
from department.models import Department
from slugify import slugify

def get_file_path(instance, filename):
    # filename = "%s.%s" % (uuid.uuid4(), filename)
    filename = "%s.%s" % (uuid.uuid4(), filename)
    return os.path.join(settings.MEDIA_ROOT, filename)

class FacultyProfile(models.Model):
    slug = models.SlugField(unique=True)
    full_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15, blank= True)
    email = models.EmailField(max_length=50, blank= True)
    job_title = models.CharField(max_length=100, blank= True)
    education = models.CharField(max_length=100, blank= True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to=get_file_path,blank=True)
    def save(self, *args, **kwargs):
        id = uuid.uuid4()
        self.slug = slugify(self.full_name + str(id))
        super(FacultyProfile, self).save(*args, **kwargs)
    
    

    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name_plural = "Faculty Profile"
