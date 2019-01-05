from django.urls import path

from . import views

urlpatterns =[ 
    path('',views.index, name='index'),
    path('exercises', views.workoutList, name='exercises'),
    path('exercise', views.apiExercise, name='apiExercise'),
    path('testJS',views.testJS, name = 'testJS'),
]
