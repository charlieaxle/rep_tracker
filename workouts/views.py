from django.shortcuts import render
from django.http import HttpResponse, QueryDict, HttpResponseBadRequest
from workouts.models import Exercise, Session, Set, Gym, Individual, ExerciseType, SummaryIndividual, Program, PlannedSets
from django.template import loader
import datetime
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
import string


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

def exerciseList(request):
    user_id = request.session['current_user_id']
    e = Exercise.objects.filter(indiv_create_id=user_id, active_ind='Y').order_by('-rec_ins_ts')
    template = loader.get_template('workouts/exercises.html')
    context  = {'exercise_list': e}
    return HttpResponse(template.render(context, request))

def programList(request):
    user_id = request.session['current_user_id']
    p = Program.objects.filter(individual_id=user_id).order_by('-rec_ins_ts')
    template = loader.get_template('workouts/programs.html')
    context  = {'program_list': p}
    return HttpResponse(template.render(context, request))


@csrf_exempt
def apiExercise(request):
    if (request.method == 'POST'):
        exercise_nm = request.POST.get("exercise_nm", "")
        if not isValid(exercise_nm, string.ascii_lowercase + string.ascii_uppercase +" "):
            return HttpResponseBadRequest('Name can only contain letters.') 
        e = Exercise()
        e.exercise_nm = exercise_nm
        e.ex_type_id = request.POST.get("ex_type_id","")
        e.rec_ins_ts = datetime.datetime.now()
        e.indiv_create_id = request.session['current_user_id']
        e.active_ind='Y'
        
        e.save()
        exercises = Exercise.objects.order_by('-rec_ins_ts')
        data = serializers.serialize('json', exercises)
        return HttpResponse(json.dumps(data), content_type="application/json")

    elif (request.method == 'PUT'):
        put = QueryDict(request.body)
        ex_id = put.get("ex_id")
        ex_nm = put.get("ex_nm")
        e = Exercise.objects.get(id=ex_id)
        e.exercise_nm = ex_nm
        e.save()
        data = serializers.serialize('json', [e,])
        return HttpResponse(json.dumps(data), content_type="application/json")

    else:
        if 'user_id' in request.GET:
            user_id = request.GET.get('user_id')
        else:
            user_id=request.session['current_user_id']
        exercises = Exercise.objects.filter(indiv_create_id=user_id, active_ind='Y').order_by('-rec_ins_ts')
        data = serializers.serialize('json', exercises)
        return HttpResponse(json.dumps(data), content_type="application/json")
        

def session(request):
    template = loader.get_template('workouts/session.html')
    user_id=request.session['current_user_id']
    exercises = Exercise.objects.filter(indiv_create_id=user_id, active_ind='Y').order_by('-rec_ins_ts')
    context = {'exercises':exercises}
    return HttpResponse(template.render(context, request))

@csrf_exempt
def apiSession(request):
    if (request.method == 'POST'):
        user_id=request.session['current_user_id']
        if not Exercise.objects.filter(indiv_create_id=user_id).exists():
            return HttpResponseBadRequest('Add exercises first!') 

        s = Session()
        s.start_ts = datetime.datetime.now()
        s.end_ts = datetime.datetime.now()
        s.individual_id = user_id
        s.gym_id = request.POST.get("gym_id","")
        s.is_open = 'Y'
        s.save()
        request.session['current_session_id'] = s.id
        print(request.session['current_session_id'])
        data =  serializers.serialize('json', [s,])
        return HttpResponse(json.dumps(data), content_type="application/json")

    elif (request.method == 'PUT'):
        individual_id = request.session['current_user_id']
        put = QueryDict(request.body)
        if 'current_session_id' in request.session:
            session_id = request.session['current_session_id']
        else:
            session_id = Session.objects.get(individual_id = individual_id, is_open = 'Y').id
        s = Session.objects.get(pk=session_id)
        s.end_ts = datetime.datetime.now()
        s.is_open = 'N'
        s.save()
        data =  serializers.serialize('json', [s,])
        return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def apiSet(request):
    if (request.method == 'POST'):
        if 'current_session_id' in request.session:
            session_id = request.session['current_session_id']
        else:
            session_id = Session.objects.get(is_open = 'Y').id
        session = Session.objects.get(id=session_id)
        session.end_ts = datetime.datetime.now()

        s = Set()
        s.weight = request.POST.get("weight","")
        s.reps = request.POST.get("reps","")
        s.exercise_id = request.POST.get("exercise_id","")
        s.session_id = session_id
        s.save()
        data =  serializers.serialize('json', [s,])
        return HttpResponse(json.dumps(data), content_type="application/json")


def isValid(input, accepted_chars):
    return all([char in accepted_chars for char in input]) and len(input)>0

@csrf_exempt
def apiIndiv(request):
    if (request.method == 'POST'):
        user_name =request.POST.get("user_nm","")

        if Individual.objects.filter(user_name = user_name).exists():
            return HttpResponseBadRequest("User Name Already Exits")

        if not isValid(user_name, string.digits + string.ascii_lowercase + string.ascii_uppercase + "_"):
            return HttpResponseBadRequest("Only Characters and Numbers allowed (No Spaces)")
        i = Individual();
        i.user_name = user_name
        i.rec_ins_ts = datetime.datetime.now()
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


@csrf_exempt
def profilePage(request):
    user_id = request.session['current_user_id']
    i = Individual.objects.get(id=user_id)

    indiv_sessions = Session.objects.filter(individual_id=user_id)    
    numSessions = indiv_sessions.count()

    times = [s.end_ts - s.start_ts for s in indiv_sessions]
    timeTotal= datetime.timedelta()
    for t in times:
        timeTotal += t

    (d,h,m) = timeTotal.days, timeTotal.seconds//3600, (timeTotal.seconds//60)%60

    context = {'indiv': i, 'numSessions':numSessions, 'timeTotal':[d,h,m] }
    
    template = loader.get_template('workouts/profilePage.html')
    return HttpResponse(template.render(context, request))



@csrf_exempt
def planView(request):
    template = loader.get_template('workouts/createPlan.html')
    return HttpResponse(template.render({}, request))

@csrf_exempt
def apiProgram(request):
    user_id = request.session['current_user_id']
    if (request.method == 'POST'):
        program_nm = request.POST.get("program_nm","")
        if program_nm == "":
            return HttpResponseBadRequest('Program Name is Empty')
        if Program.objects.filter(program_nm = program_nm, individual_id =user_id ).exists():
            return HttpResponseBadRequest('Program Name is Duplicate')
        print(program_nm)
        p = Program()
        p.program_nm = program_nm
        p.individual_id = user_id
        p.rec_ins_ts = datetime.datetime.now()
        p.save()
        data =  serializers.serialize('json', [p,])
        return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def apiPlannedSets(request):
    if (request.method == 'POST'):
        program_id = request.POST.get("program_id","")
        exercise_id = request.POST.get("ex_id","")
        num_sets = request.POST.get("num_sets","")
        prog_order_nbr = request.POST.get("prog_order_nbr","")
        ps = PlannedSets()
        ps.program_id = program_id
        ps.exercise_id = exercise_id
        ps.num_sets = num_sets
        ps.prog_order_nbr = prog_order_nbr
        ps.save()
        data =  serializers.serialize('json', [ps,])
        return HttpResponse(json.dumps(data), content_type="application/json")


@csrf_exempt
def startProgram(request):
    if 'program_id' in request.GET:
        user_id = request.session["current_user_id"]
        program_id = request.GET.get("program_id","")
        print('here:',request.GET.get("program_id",""))
        p = Program.objects.get(id=program_id)
        ps = p.plannedsets_set.order_by('id').distinct()
        plannedSets = []
        for plannedSet in ps:
            for i in range(plannedSet.num_sets):
                tmp = {}
                tmp["exercise_nm"] = plannedSet.exercise.exercise_nm	
                tmp["exercise_id"] = plannedSet.exercise_id
                plannedSets.append(tmp)
        exercises = Exercise.objects.filter(indiv_create_id=user_id, active_ind='Y').order_by('-rec_ins_ts')   
        context = {'plannedSets':plannedSets, 'exercises':exercises}
        template = loader.get_template('workouts/createWorkout.html')
        return HttpResponse(template.render(context, request))
    else:
        user_id = request.session["current_user_id"]
        exercises = Exercise.objects.filter(indiv_create_id=user_id, active_ind='Y').order_by('-rec_ins_ts') 
        context = {'plannedSets':{}, 'exercises':exercises}
        template = loader.get_template('workouts/createWorkout.html')
        return HttpResponse(template.render(context, request))


@csrf_exempt
def workoutTransition(request):
    template = loader.get_template('workouts/startWorkoutTransition.html')
    return HttpResponse(template.render({}, request))
  

