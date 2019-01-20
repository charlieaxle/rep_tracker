from django.db import models
import datetime

# Create your models here.

class Individual(models.Model):
    #first_nm = models.CharField(max_length=200)
    #last_nm = models.CharField(max_length=200)
    #email_addr_txt = models.CharField(max_length=200)
    rec_ins_ts = models.DateTimeField()
    user_name = models.CharField(max_length=50, unique=True);

    def has_open_session(self):
        return self.session_set.filter(is_open = 'Y')
        

class SummaryIndividual(models.Model):
    #first_nm = models.CharField(max_length=200)
    #last_nm = models.CharField(max_length=200)
    #email_addr_txt = models.CharField(max_length=200)
    rec_ins_ts = models.DateTimeField()
    user_name = models.CharField(max_length=50, unique=True);
    num_workouts = models.IntegerField(default = 0);
    total_time = models.DateTimeField();
    


class Gym(models.Model):
    gym_nm = models.CharField(max_length=200)
    rec_ins_ts = models.DateTimeField()

class ExerciseType(models.Model):
    ex_type_cd = models.CharField(max_length=2)
    ex_type_desc = models.CharField(max_length=200)  

class Exercise(models.Model):
    exercise_nm = models.CharField(max_length=200)
    ex_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)
    rec_ins_ts = models.DateTimeField()
    indiv_create = models.ForeignKey(Individual, on_delete=models.CASCADE)
    active_ind = models.CharField(max_length = 1)

class Session(models.Model):
    individual = models.ForeignKey(Individual, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, null=True)
    start_ts = models.DateTimeField()
    end_ts = models.DateTimeField(blank=True, null=True)
    is_open = models.CharField(max_length=1, default ='N')

    def get_session_duration(self):
        duration = self.end_ts - self.start_ts
        (d,h,m) = duration.days, duration.seconds//3600, (duration.seconds//60)%60
        return {"hours":h, "minutes":"{:02d}".format(m)}
        


class Set(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, default=999)
    reps = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

