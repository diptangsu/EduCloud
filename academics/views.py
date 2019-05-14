from django.shortcuts import render
from django.shortcuts import Http404

from questions.models import Question
from users.models import User

from academics.models import Department
from academics.models import Subject

from educloud.decorators import login_required


@login_required
def department_questions(request, department: str):
    department = department.upper()
    questions = Question.objects.filter(subject__department__short_form=department).order_by('-timestamp')

    departments = Department.objects.all()

    department_obj = Department.objects.get(short_form=department)
    header = department_obj.name

    return render(request, 'questions/questions.html', {
        'questions': questions,
        'department': department,
        'title': department,
        'departments': departments,
        'header': header
    })


def subject_questions(request, subject_code: str):
    subject_code = subject_code.upper()
    questions = Question.objects.filter(subject__code=subject_code).order_by('-timestamp')

    departments = Department.objects.all()
    title = subject_code

    try:
        subject = Subject.objects.get(code=subject_code)
    except Subject.DoesNotExist:
        raise Http404

    header = subject.name

    return render(request, 'questions/questions.html', {
        'questions': questions,
        'departments': departments,
        'header': header,
        'title': title
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
