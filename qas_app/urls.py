from django.urls import path
from .views import QuestionListView, QuestionDetailView
from . import views

urlpatterns = [
    path('', QuestionListView.as_view(), name='qas-home'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('profile/', views.profile, name='profile'),
    path('inbox/', views.inbox, name='inbox'),
    path('friends/', views.friends, name='friends'),
    path('notifications/', views.notifications, name='notifications'),
]