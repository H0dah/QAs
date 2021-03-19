from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def home(request):
    all_questions = Question.objects.all()
    context = {
        'questions': all_questions        
    }
    return render(request, 'qas_app/home.html', context)

def profile(request):
    return render(request,'qas_app/profile.html', {'title':'profile' } )

def inbox(request):
    return render(request,'qas_app/inbox.html', {'title':'inbox'} )

def friends(request):
    return render(request,'qas_app/friends.html', {'title':'friends'} )

def notifications(request):
    return render(request,'qas_app/notifications.html', {'title':'notifications'} )