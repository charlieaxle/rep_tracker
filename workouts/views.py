from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from workouts.models import Exercise, Session, Set, Gym, Individual
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
        data = serializers.serialize('json', exercises)
        return HttpResponse(json.dumps(data), content_type="application/json")
        

    else: 
        exercises = Exercise.objects.order_by('-rec_ins_ts')
        data = serializers.serialize('json', exercises)
        return HttpResponse(json.dumps(data), content_type="application/json")
        

def home(request):
    template = loader.get_template('workouts/home.html')
    return HttpResponse(template.render({}, request))

def session(request):
    template = loader.get_template('workouts/session.html')
    exercises = Exercise.objects.order_by('-rec_ins_ts')
    context = {'exercises':exercises}
    return HttpResponse(template.render(context, request))

@csrf_exempt
def apiSession(request):
    if (request.method == 'POST'):
        s = Session()
        s.start_ts = datetime.datetime.now()
        s.individual_id = request.POST.get("individual_id","")
        s.gym_id = request.POST.get("gym_id","")
        s.save()
        data =  serializers.serialize('json', [s,])
        return HttpResponse(json.dumps(data), content_type="application/json")

    elif (request.method == 'PUT'):
        put = QueryDict(request.body)
        session_id = put.get("session_id")
        s = Session.objects.get(pk=session_id)
        s.end_ts = datetime.datetime.now()
        s.save()
        data =  serializers.serialize('json', [s,])
        return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def apiSet(request):
    if (request.method == 'POST'):
        s = Set()
        s.exercise_id = request.POST.get("exercise_id","")
        s.weight = request.POST.get("weight","")
        s.reps = request.POST.get("reps","")
        s.session_id = request.POST.get("session_id","")
        s.save()
        data =  serializers.serialize('json', [s,])
        return HttpResponse(json.dumps(data), content_type="application/json")
