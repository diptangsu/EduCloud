from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import Http404
from django.shortcuts import redirect

from questions.models import Question
from questions.models import Answer
from questions.models import QuestionVote
from questions.models import AnswerVote

from .models import User


def login(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        try:
            user = User.objects.get(email_id=email, password=password)
        except User.DoesNotExist:
            try:
                user_ = User.objects.get(email_id=email)
                return render(request, 'users/login.html', {
                    'email': user_.email_id
                })
            except User.DoesNotExist:
                return redirect('user-register')

        request.session['user_id'] = user.id

        department_short_form = user.department.short_form
        return redirect(f'/academics/department/{department_short_form}/questions')
    else:
        raise Http404


def logout(request):
    if request.method == 'POST':
        del request.session['user_id']
        return redirect('all-questions-home')
    else:
        raise Http404


def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')
    elif request.method == 'POST':
        # fetch user details
        # save data
        user_id = 1
        user_type = 'S'

        if user_type == 'S':
            return redirect(f'/student-register/{user_id}')
        else:
            return redirect(f'/professor-register/{user_id}')
    else:
        raise Http404


def student_register(request, user_id):
    if request.method == 'GET':
        return render(request, 'users/student-details-register.html')
    elif request.method == 'POST':
        # fetch student details
        # save data
        return redirect('user-login')
    else:
        raise Http404


def professor_register(request, user_id):
    if request.method == 'GET':
        return render(request, 'users/professor-details-register.html')
    elif request.method == 'POST':
        # fetch professor details
        # save data
        return redirect('user-login')
    else:
        raise Http404


def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if user.user_type == 'S':
        return render(request, 'users/student-profile.html', {
            'user': user
        })
    else:
        return render(request, 'users/professor-profile.html', {
            'user': user
        })


def user_questions(request, user_id):
    questions = Question.objects.filter(user_id=user_id)

    return render(request, 'academics/questions.html', {
        'questions': questions
    })


def user_answers(request, user_id):
    answers = Answer.objects.filter(user_id=user_id)

    return render(request, 'users/user-answers.html', {
        'answers': answers
    })
