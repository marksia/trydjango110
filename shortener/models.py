import random
import string

from django.db import models

from .utils import code_generator, create_shortcode
# Create your models here.

class KirrURL(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True) # when model was created
    updated = models.DateTimeField(auto_now_add=True) # everytime the model is saved
    # empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    # shortcode = models.CharField(max_length=15, null=True) Empty in database is okay
    # shortcode = models.CharField(max_length=15, default='cfedefaultshortcode')

    def __str__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(KirrURL, self).save(*args, **kwargs)

