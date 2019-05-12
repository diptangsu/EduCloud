from django.db import models

from academics.models import Subject


class Question(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} [{self.user.first_name}, {self.subject.code}]'

    def votes(self):
        upvotes = QuestionVote.objects.filter(question=self, vote_type='U').count()
        downvotes = QuestionVote.objects.filter(question=self, vote_type='D').count()

        return upvotes - downvotes


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

    class Meta:
        unique_together = ('question', 'user')

    def __str__(self):
        return f'{self.get_vote_type_display()}: {self.user.first_name}, {self.question}'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.first_name}: {self.question.name}'

    def votes(self):
        upvotes = AnswerVote.objects.filter(answer=self, vote_type='U').count()
        downvotes = AnswerVote.objects.filter(answer=self, vote_type='D').count()

        return upvotes - downvotes


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

    class Meta:
        unique_together = ('answer', 'user')

    def __str__(self):
        return f'{self.get_vote_type_display()}: {self.user.first_name}, {self.answer}'

