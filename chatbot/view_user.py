from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import User
from .form import MyUserCreationForm


def signup(request):
   form = MyUserCreationForm()
   
   if request.method == 'POST':
       form = MyUserCreationForm(request.POST)
       if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username,
                                    password=request.POST['password1'])
            login(request, user)
            return redirect('title-learn')

   return render(request, 'registration/signup.html', { 'form':  form})


