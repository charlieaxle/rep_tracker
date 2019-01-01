from django.db import models

# Create your models here.

class Gym(models.Model):
    gym_nm = models.CharField(max_length=200)
    rec_ins_ts = models.DateTimeField()

class Exercise(models.Model):
    exercise_nm = models.CharField(max_length=200)
    ex_type_cd = models.CharField(max_length=3)
    rec_ins_ts = models.DateTimeField()

class Sets(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.IntegerField(default=0)

