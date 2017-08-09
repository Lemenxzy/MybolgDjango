# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Home(models.Model):
    ipadress = models.CharField(max_length=20)