from django.urls import path
from .views import *
urlpatterns =[
    path('chat',actionChat, name='chat'),
    path('title-learn',titleLearn, name='title-learn'),
]