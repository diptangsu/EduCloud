from django.shortcuts import render

from questions.models import Question
from questions.models import Answer
from questions.models import QuestionVote
from questions.models import AnswerVote


def login(request):
    pass


def logout(request):
    pass


def register(request):
    pass


def student_register(request, user_id):
    pass


def professor_register(request, user_id):
    pass


def profile(request, user_id):
    pass


def questions(request, user_id):
    pass


def answers(request, user_id):
    pass


def reputation(self):
    questions = Question.objects.filter(user=self)
    answers = Answer.objects.filter(user=self)

    rep = 0

    for question in questions:
        question_upvotes = QuestionVote.objects.filter(question=question, vote_type='U')
        question_downvotes = QuestionVote.objects.filter(question=question, vote_type='D')

        rep += len(question_upvotes) * 10
        rep -= len(question_downvotes) * 1

    for answer in answers:
        answer_upvotes = AnswerVote.objects.filter(answer=answer, vote_type='U')
        answer_downvotes = AnswerVote.objects.filter(answer=answer, vote_type='D')

        rep += len(answer_upvotes) * 20
        rep -= len(answer_downvotes) * 2

    return rep
