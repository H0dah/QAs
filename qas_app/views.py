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

#Questions viewed in Home Page
class QuestionListView(ListView):
    model = Question
    template_name = 'qas_app/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'questions'
    paginate_by = 7


    def get_queryset(self):
        return Question.objects.all().exclude(answer = '').order_by('-date_posted')
        

# for questions that asked to loged in user ( shown in questions page)
class QuestionsView(ListView):
    model = Question
    template_name = 'qas_app/questions.html'
    context_object_name = 'questions'
    paginate_by = 7

    def get_queryset(self):
        user = self.request.user
        return Question.objects.filter(asked_user=user).filter(answer= '').order_by('-date_posted')


class QuestionDetailView(DetailView):
    model = Question


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['text', 'asked_user']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AnswerQuestion(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields = ['answer']
    success_url = '/questions'
    template_name = 'qas_app/answer_question.html'

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.asked_user:
            return True
        return False


# user profile page
class UserProfile(ListView):
    model = Question
    template_name = 'qas_app/user_profile.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'questions'
    paginate_by = 7

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Question.objects.filter(asked_user=user).exclude(answer = '').order_by('-date_posted')#create field for quetion date 