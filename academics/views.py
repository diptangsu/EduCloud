from django.shortcuts import render

from questions.models import Question


def questions(request, dept):
    all_questions = Question.objects.filter(subject__department__short_form=dept).order_by('timestamp')
    return render(request, 'academics/dept-questions.html', {
        'all_questions': all_questions
    })


def professors(request, dept):
    pass


def students(request, dept):
    pass
