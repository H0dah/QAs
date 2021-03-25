from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Question
from django.views.generic import(
     ListView,
     DetailView,
     CreateView,
     UpdateView,
     DeleteView
)


class QuestionListView(ListView):
    model = Question
    template_name = 'qas_app/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'questions'
    

    def get_queryset(self):
        return Question.objects.all().exclude(answer = '')
        
    ordering = ['-date_posted']
    paginate_by = 7

class UserQuestionListView(ListView):
    model = Question
    template_name = 'qas_app/user_questions.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'questions'
    paginate_by = 7

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Question.objects.filter(author=user).order_by('-date_posted')

class QuestionDetailView(DetailView):
    model = Question

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['text']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields = ['text']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False


class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    success_url = '/'

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False



def profile(request):
    return render(request,'qas_app/profile.html', {'title':'profile' } )

def inbox(request):
    return render(request,'qas_app/inbox.html', {'title':'inbox'} )

def friends(request):
    return render(request,'qas_app/friends.html', {'title':'friends'} )

def notifications(request):
    return render(request,'qas_app/notifications.html', {'title':'notifications'} )