from django.db import models

from academics.models import Subject


class Question(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class QuestionImage(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='question_images/')


class QuestionVote(models.Model):
    VOTE_TYPES = (
        ('U', 'UpVote'),
        ('D', 'DownVote')
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
    vote_type = models.CharField(max_length=1, choices=VOTE_TYPES)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class AnswerImage(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='answer_images/')


class AnswerVote(models.Model):
    VOTE_TYPES = (
        ('U', 'UpVote'),
        ('D', 'DownVote')
    )
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
    vote_type = models.CharField(max_length=1, choices=VOTE_TYPES)
