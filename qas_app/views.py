from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Question, Friend_Request
from django.contrib.auth.decorators import login_required
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
        return Question.objects.all().exclude(answer = '').order_by('-date_answered')
        

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
    template_name = 'qas_app/user_profile.html'
    paginate_by = 7

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['user_object']= User.objects.get(username=self.kwargs.get('username'))
        return context
        

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Question.objects.filter(asked_user=user).exclude(answer = '').order_by('-date_answered')



@login_required
def send_friend_request(request, userID):

    to_user = User.objects.get(id=userID)

    #when user try to send request to himslef, Security Consideration :)) 
    if request.user == to_user:
        return HttpResponse('friend request sent')

    _, created = Friend_Request.objects.get_or_create(
        from_user=request.user, to_user=to_user
    )
    if created:
        return HttpResponse('friend request sent')

    else:
        return HttpResponse('friend request was already sent')

#need editing dude :) 
@login_required
def accept_friend_request(request, requestID):
    friend_request = Friend_Request.objects.get(id=requestID)
    if friend_request.to_user == request.user:
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.delete()
        return HttpResponse('friend request accepted')
    else:
        return HttpResponse('friend request not accepted')