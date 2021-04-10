from django.urls import path
from .views import (
    QuestionListView,
    QuestionsView,
    QuestionDetailView,
    QuestionCreateView,
    AnswerQuestion,
    UserProfile,
)

urlpatterns = [
    path('', QuestionListView.as_view(), name='qas-home'),
    path('questions/', QuestionsView.as_view(), name ='questions'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('question/new/', QuestionCreateView.as_view(), name='question-create'),
    path('question/<int:pk>/answer', AnswerQuestion.as_view(), name='answer-question'),
    path('<str:username>/', UserProfile.as_view(), name='user-profile'),

]