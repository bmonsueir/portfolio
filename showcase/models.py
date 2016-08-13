from __future__ import unicode_literals
from django.shortcuts import render

from django.db import models

class Work(models.Model):
    image = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    linkTo = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title
