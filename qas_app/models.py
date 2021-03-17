from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

DEFAULT_author_ID = 1
class Question(models.Model):
    text = models.CharField(max_length=100)
    answer = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=DEFAULT_author_ID)
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.text