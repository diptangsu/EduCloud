from django.shortcuts import render

from questions.models import Question
from users.models import User


def department_questions(request, department: str):
    department = department.upper()
    print(department)
    questions = Question.objects.filter(subject__department__short_form=department).order_by('-timestamp')

    return render(request, 'academics/questions.html', {
        'questions': questions
    })


def subject_questions(request, subject_code: str):
    subject_code = subject_code.upper()
    questions = Question.objects.filter(subject__code=subject_code).order_by('-timestamp')

    return render(request, 'academics/questions.html', {
        'questions': questions
    })


def department_professors(request, department: str):
    department = department.upper()
    professors = User.objects.filter(user_type='P', department__short_form=department)

    return render(request, 'academics/professors.html', {
        'professors': professors
    })


def all_professors(request):
    professors = User.objects.filter(user_type='P').order_by('department__short_form')

    return render(request, 'academics/professors.html', {
        'professors': professors
    })
