from django.shortcuts import render

# Create your views here.
def titleLearn(request):
    return render(request,'title.html')

def actionChat(request):
    return render(request,'chat.html')