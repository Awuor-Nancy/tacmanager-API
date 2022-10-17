from django.db import models

# Create your models here.
class Bills(models.Model):
    title = models.CharField(max_length=255)
    amount = models.FloatField()

class Tax(models.Model):
    title = models.CharField(max_length=255)
    amount = models.FloatField()

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    



