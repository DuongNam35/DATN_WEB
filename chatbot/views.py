from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def titleLearn(request):
    return render(request,'title.html')

@login_required
def actionChat(request):
    return render(request,'chat.html')

@login_required
def indexView(request):
    return render(request, 'index.html')

@login_required
def conFig(request):
    return render(request,'config.html')