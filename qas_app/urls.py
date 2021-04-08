from django.urls import path
from .views import (
    QuestionListView,
    QuestionDetailView,
    QuestionCreateView,
    AnswerQuestion,
    UserQuestionListView,
    QuestionsView,
    profile,
    inbox,
    friends,
    notifications
)

urlpatterns = [
    path('', QuestionListView.as_view(), name='qas-home'),
    path('questions/', QuestionsView.as_view(), name ='questions'),
    path('question/<int:pk>/answer', AnswerQuestion.as_view(), name='answer-question'),
    path('user/<str:username>/', UserQuestionListView.as_view(), name='user-question'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('question/new/', QuestionCreateView.as_view(), name='question-create'),
    path('inbox/', inbox, name='inbox'),
    path('friends/', friends, name='friends'),
    path('notifications/', notifications, name='notifications'),
]