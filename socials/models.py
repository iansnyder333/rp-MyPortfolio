from django.db import models




class Social(models.Model):
    network = models.CharField(max_length=100)
    link = models.URLField(max_length=100)
    image = models.FilePathField(path="/img")
