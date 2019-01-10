from django.db import models

# Create your models here.

class Individual(models.Model):
    #first_nm = models.CharField(max_length=200)
    #last_nm = models.CharField(max_length=200)
    #email_addr_txt = models.CharField(max_length=200)
    rec_ins_ts = models.DateTimeField()
    user_name = models.CharField(max_length=50);

class Gym(models.Model):
    gym_nm = models.CharField(max_length=200)
    rec_ins_ts = models.DateTimeField()

class Exercise(models.Model):
    exercise_nm = models.CharField(max_length=200)
    ex_type_cd = models.CharField(max_length=3)
    rec_ins_ts = models.DateTimeField()

class Session(models.Model):
    individual = models.ForeignKey(Individual, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, null=True)
    start_ts = models.DateTimeField()
    end_ts = models.DateTimeField(blank=True, null=True)


class Set(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, default=999)
    reps = models.IntegerField(default=0)
    weight = models.IntegerField()

