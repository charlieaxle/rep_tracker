from django.urls import path

from . import views

urlpatterns =[ 
    path('',views.index, name='index'),
    path('exercises', views.workoutList, name='exercises'),
    path('exercise', views.apiExercise, name='apiExercise'),
    path('home',views.home, name = 'home'),
    path('session', views.session, name='workoutSession'),
    path('api/set', views.apiSet, name='apiSet'),
    path('api/session',views.apiSession, name='apiSession'),
    path('session_summary/<int:session_id>', views.sessionSummary, name='sessionSummary'),
    path('api/individual', views.apiIndiv, name='apiIndiv'),
    path('api/signOut', views.signOut, name='apiSignOut'),
    path('history', views.historySummary, name='historySummary'),
]
