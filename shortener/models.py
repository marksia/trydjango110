import random
import string

from django.db import models

# Create your models here.


def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    # new_code = ''
    # for _ in range(size):
    #     new_code += random.choice(chars)
    # return new_code
    return ''.join(random.choice(chars) for _ in range(size))


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

    def save(self, *args, **kwargs):
        print("something")
        self.shortcode = code_generator()
        super(KirrURL, self).save(*args, **kwargs)

