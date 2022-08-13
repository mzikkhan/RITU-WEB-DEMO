"""Defines URL patterns for ritu_web_app"""

from django.urls import path

from . import views

app_name= 'ritu_web_app'
urlpatterns=[
    # Home page
    path('', views.homepage, name='homepage'),
    path('aboutUs',views.aboutUs,name='aboutUs'),
    path('contactUs',views.contactUs,name='contactUs'),
    path('finalMessage',views.finalMessage,name='finalMessage'),
    path('leaderboard',views.leaderboard,name='leaderboard'),
    path('marketplace',views.marketplace,name='marketplace'),

    path('task1',views.task1,name='task1'),
    path('task2',views.task2,name='task2'),
    path('task3',views.task3,name='task3'),
    path('verification',views.verification,name='verificationPage'),
    path('profile',views.profileCard,name='profileCard'),
    path('FinalMessege',views.FinalMessege,name='FinalMessege'),
]
