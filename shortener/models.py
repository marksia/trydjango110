from django.db import models

# Create your models here.


class KirrURL(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15, unique=True)
    timestamp = models.DateTimeField(auto_now=True) # when model was created
    updated = models.DateTimeField(auto_now_add=True) # everytime the model is saved
    # empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    # shortcode = models.CharField(max_length=15, null=True) Empty in database is okay
    # shortcode = models.CharField(max_length=15, default='cfedefaultshortcode')

    def __str__(self):
        return str(self.url)
