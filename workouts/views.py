from django.shortcuts import render
from django.http import HttpResponse
from workouts.models import Exercise
from django.template import loader
import datetime
from workouts.forms import ExerciseForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers

def index(request):
    return HttpResponse("Workout index")

def workoutList(request):
    e = Exercise.objects.order_by('-rec_ins_ts')
    template = loader.get_template('workouts/exercises.html')
    context  = {'exercise_list': e}
    return HttpResponse(template.render(context, request))

@csrf_exempt
def apiExercise(request):
    if (request.method == 'POST'): 
        e = Exercise()
        e.exercise_nm = request.POST.get("exercise_nm", "")
        e.ex_type_cd = request.POST.get("ex_type_cd","")
        e.rec_ins_ts = datetime.datetime.now()
        e.save()
        exercises = Exercise.objects.order_by('-rec_ins_ts')
        data = data = serializers.serialize('json', exercises)
        return HttpResponse(json.dumps(data), content_type="application/json")
        

    else: 
        exercises = Exercise.objects.order_by('-rec_ins_ts')
        data = serializers.serialize('json', exercises)
        return HttpResponse(json.dumps(data), content_type="application/json")
        

def testJS(request):
    template = loader.get_template('workouts/testJS.html')
    return HttpResponse(template.render({}, request))
