from django.shortcuts import render
from django.http import HttpResponse

#dummy data, list of dictionaries 
posts = [
    {
        #'key': 'value'
        'question': 'what\'s your name',
        'answer': 'hoda'
    },
    {
        'question': 'what\'s your age',
        'answer': '22'
    }

]

def home(request):
    context = {
        'posts': posts,
        'title': 'Feed'
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