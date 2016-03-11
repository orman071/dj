from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=254)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    rating = models.IntegerField(blank=True, null=True)
    author = models.ForeignKey(User, related_name='+')
    likes = models.ManyToManyField(User, related_name='+')


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

# Create your models here.
