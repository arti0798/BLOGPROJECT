# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# one to one realationship

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # if the user get deleted profile will also get deleted (cascade)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' 
        # return f'{self.user.username} Profile'
        # return self.user.username

    def save(self):    
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



