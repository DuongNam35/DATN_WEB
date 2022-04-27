from django.urls import path,include
from .view_user import *
from .views import *
urlpatterns =[
    path('',indexView,name='main'),
    path('accounts/', include('django.contrib.auth.urls'), name=login),
    path('accounts/signup', signup, name='signup'), 

    path('chat',actionChat, name='chat'),
    path('title-learn',titleLearn, name='title-learn'),

    path('config',conFig,name="config")
]