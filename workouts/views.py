from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from workouts.models import Exercise, Session, Set, Gym, Individual, ExerciseType
from django.template import loader
import datetime
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers


@csrf_exempt
def index(request):
    if 'current_user_id' in request.session:
        template = loader.get_template('workouts/home.html')
        user_id = request.session['current_user_id']
        i = Individual.objects.get(id = user_id)
        context = {"individual":i}
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('workouts/login.html')
        return HttpResponse(template.render({}, request))

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
        e.ex_type_id = request.POST.get("ex_type_id","")
        e.rec_ins_ts = datetime.datetime.now()
        e.indiv_create_id = request.session['current_user_id']
        e.save()
        exercises = Exercise.objects.order_by('-rec_ins_ts')
        data = serializers.serialize('json', exercises)
        return HttpResponse(json.dumps(data), content_type="application/json")
        

    else: 
        exercises = Exercise.objects.order_by('-rec_ins_ts')
        data = serializers.serialize('json', exercises)
        return HttpResponse(json.dumps(data), content_type="application/json")
        
@csrf_exempt
def home(request):
    template = loader.get_template('workouts/home.html')
    user_id = request.session['current_user_id']
    i = Individual.objects.get(id = user_id)
    context = {"individual":i}
    return HttpResponse(template.render(context, request))

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
        s.individual_id = request.session['current_user_id']
        s.gym_id = request.POST.get("gym_id","")
        s.save()
        request.session['current_session_id'] = s.id
        print(request.session['current_session_id'])
        data =  serializers.serialize('json', [s,])
        return HttpResponse(json.dumps(data), content_type="application/json")

    elif (request.method == 'PUT'):
        put = QueryDict(request.body)
        session_id = request.session['current_session_id']
        s = Session.objects.get(pk=session_id)
        s.end_ts = datetime.datetime.now()
        s.save()
        data =  serializers.serialize('json', [s,])
        return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def apiSet(request):
    if (request.method == 'POST'):
        s = Set()
        s.weight = request.POST.get("weight","")
        s.reps = request.POST.get("reps","")
        s.exercise_id = request.POST.get("exercise_id","")
        s.session_id = request.session['current_session_id']
        s.save()
        data =  serializers.serialize('json', [s,])
        return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def apiIndiv(request):
    if (request.method == 'POST'):
        i = Individual();
        i.rec_ins_ts = datetime.datetime.now()
        i.user_name =request.POST.get("user_nm","")
        i.save()
        request.session['current_user_id'] = i.id
        data =  serializers.serialize('json', [i,])
        return HttpResponse(json.dumps(data), content_type="application/json")
    elif (request.method == 'GET'):
        user_nm = request.GET.get("user_nm")
        i = Individual.objects.get(user_name = user_nm)
        request.session['current_user_id'] = i.id
        data =  serializers.serialize('json', [i,])
        return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def signOut(request):
        request.session.flush()
        template = loader.get_template('workouts/login.html')
        return HttpResponse('logged out')
	


@csrf_exempt
def sessionSummary(request, session_id):
    session = Session.objects.get(id=session_id)
    template =  loader.get_template('workouts/session_summary.html')
    context = {'session': session}
    return HttpResponse(template.render(context, request))


@csrf_exempt
def historySummary(request):
    user_id = request.session['current_user_id']
    current_user = Individual.objects.get(id=user_id)
    context = {'current_user': current_user}
    template = loader.get_template('workouts/historySummary.html')
    return HttpResponse(template.render(context, request))

@csrf_exempt
def addExercise(request):
    exercise_types = ExerciseType.objects.all();
    context = {'exercise_types':exercise_types}
    template = loader.get_template('workouts/addExercise.html')
    return HttpResponse(template.render(context, request))
 
