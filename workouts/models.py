from django.db import models

# Create your models here.

class Gym(models.Model):
    gym_nm = models.CharField(max_length=200)
    rec_ins_ts = models.DateTimeField()


