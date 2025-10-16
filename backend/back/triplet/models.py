from django.db import models

# Create your models here.
class triplets(models.Model):
    ab=models.FloatField()
    bc=models.FloatField()
    ac=models.FloatField()
