# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Upload(models.Model):
    upload_file = models.FileField(upload_to='uploads')


class DropboxInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=200)
