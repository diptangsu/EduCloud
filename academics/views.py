from django.shortcuts import render

from questions.models import Question
from users.models import User

from academics.models import Department


def department_questions(request, department: str):
    department = department.upper()
    questions = Question.objects.filter(subject__department__short_form=department).order_by('-timestamp')

    departments = Department.objects.all()

    department_obj = Department.objects.get(short_form=department)
    header = department_obj.name

    return render(request, 'academics/questions.html', {
        'questions': questions,
        'department': department,
        'departments': departments,
        'header': header
    })


def subject_questions(request, subject_code: str):
    subject_code = subject_code.upper()
    questions = Question.objects.filter(subject__code=subject_code).order_by('-timestamp')

    departments = Department.objects.all()

    return render(request, 'academics/questions.html', {
        'questions': questions,
        'departments': departments
    })


def department_professors(request, department: str):
    department = department.upper()
    professors = User.objects.filter(user_type='P', department__short_form=department)

    departments = Department.objects.all()

    return render(request, 'academics/professors.html', {
        'professors': professors,
        'departments': departments
    })


def all_professors(request):
    professors = User.objects.filter(user_type='P').order_by('department__short_form')

    return render(request, 'academics/professors.html', {
        'professors': professors
    })
