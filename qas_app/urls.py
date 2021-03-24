from django.urls import path
from .views import (
    QuestionListView,
    QuestionDetailView,
    QuestionCreateView,
    QuestionUpdateView,
    QuestionDeleteView,
    profile,
    inbox,
    friends,
    notifications
)

urlpatterns = [
    path('', QuestionListView.as_view(), name='qas-home'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('question/new/', QuestionCreateView.as_view(), name='question-create'),
    path('question/<int:pk>/update/', QuestionUpdateView.as_view(), name='question-update'),
    path('question/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question-delete'),
    path('profile/', profile, name='profile'),
    path('inbox/', inbox, name='inbox'),
    path('friends/', friends, name='friends'),
    path('notifications/', notifications, name='notifications'),
]