from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Question(models.Model):
    text = models.CharField(max_length=100)
    answer = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    asked_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'asked')
    date_posted = models.DateTimeField(default=timezone.now)
    date_answered = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('question-detail', kwargs={'pk': self.pk})

class Friend_Request(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)