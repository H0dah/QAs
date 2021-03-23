from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.views.generic import ListView, DetailView


def home(request):
    context = {
        'questions': Question.objects.all()      
    }
    return render(request, 'qas_app/home.html', context)

class QuestionListView(ListView):
    model = Question
    template_name = 'qas_app/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'questions'
    ordering = ['-date_posted']

class QuestionDetailView(DetailView):
    model = Question


def profile(request):
    return render(request,'qas_app/profile.html', {'title':'profile' } )

def inbox(request):
    return render(request,'qas_app/inbox.html', {'title':'inbox'} )

def friends(request):
    return render(request,'qas_app/friends.html', {'title':'friends'} )

def notifications(request):
    return render(request,'qas_app/notifications.html', {'title':'notifications'} )