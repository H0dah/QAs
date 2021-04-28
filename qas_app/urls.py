from django.urls import path
from .views import (
    QuestionListView,
    QuestionsView,
    QuestionDetailView,
    QuestionCreateView,
    AnswerQuestion,
    UserProfile,
    send_friend_request,
    accept_friend_request,
)

urlpatterns = [
    path('', QuestionListView.as_view(), name='qas-home'),
    path('questions/', QuestionsView.as_view(), name ='questions'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('question/new/', QuestionCreateView.as_view(), name='question-create'),
    path('question/<int:pk>/answer', AnswerQuestion.as_view(), name='answer-question'),
    path('<str:username>/', UserProfile.as_view(), name='user-profile'),
    path('send_friend_request/<int:userID>/', send_friend_request, name='send-friend-request'),
    path('accept_friend_request/<int:requestID>/', accept_friend_request, name='accept-friend-request'),
]