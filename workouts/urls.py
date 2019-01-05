from django.urls import path

from . import views

urlpatterns =[ 
    path('',views.index, name='index'),
    path('exercises', views.workoutList, name='exercises'),
    path('new_exercise', views.newExercise, name='newExercise'),
    path('testJS',views.testJS, name = 'testJS'),
]
