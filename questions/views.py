from django.shortcuts import render

from .models import Question


def questions(request):
    all_questions = Question.objects.all().order_by('timestamp')
    return render(request, 'questions/all-questions.html', {
        'all_questions': all_questions
    })
