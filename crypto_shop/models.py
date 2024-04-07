from django.db import models

class Reviews(models.Model):
    name = models.CharField(max_length=50)
    proffession = models.CharField(max_length=50)
    comment = models.TextField()