from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import Http404
from django.shortcuts import redirect

from django.contrib import messages

from questions.models import Question
from questions.models import Answer
from academics.models import Department

from .models import User
from educloud.decorators import login_required


def login(request):
    if 'user_id' in request.session:
        try:
            user = User.objects.get(id=request.session.get('user_id'))
            department_short_form = user.department.short_form
            return redirect(f'/academics/department/{department_short_form}/questions')
        except User.DoesNotExist:
            pass

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
                messages.add_message(request, messages.ERROR, 'Incorrect Password')
                return render(request, 'users/login.html', {
                    'email': user_.email_id
                })
            except User.DoesNotExist:
                messages.add_message(request, messages.ERROR, 'User not registered')
                return redirect('user-register')

        request.session['user_id'] = user.id

        department_short_form = user.department.short_form
        return redirect(f'/academics/department/{department_short_form}/questions')
    else:
        raise Http404


@login_required
def logout(request):
    if request.method == 'POST':
        del request.session['user_id']
        return redirect('user-login')
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


@login_required
def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)

    logged_in_user = User.objects.get(id=request.session['user_id'])
    departments = Department.objects.all()

    if user.user_type == 'S':
        return render(request, 'users/student-profile.html', {
            'user': user,
            'logged_in_user': logged_in_user,
            'departments': departments
        })
    else:
        return render(request, 'users/professor-profile.html', {
            'user': user,
            'logged_in_user': logged_in_user,
            'departments': departments
        })


@login_required
def user_questions(request, user_id):
    questions = Question.objects.filter(user_id=user_id)
    departments = Department.objects.all()

    user = User.objects.get(id=user_id)

    header = f'All questions of {user.name()}'
    title = f'{user.first_name}\'s Questions'

    logged_in_user = User.objects.get(id=request.session['user_id'])
    user_questions_ = {
        q.id
        for q in Question.objects.filter(user_id=logged_in_user)
    }

    return render(request, 'questions/questions.html', {
        'questions': questions,
        'departments': departments,
        'header': header,
        'title': title,
        'user': user,
        'logged_in_user': logged_in_user,
        'questions_upvoted': logged_in_user.question_upvotes(),
        'questions_downvoted': logged_in_user.question_downvotes(),
        'user_questions': user_questions_
    })


@login_required
def user_answers(request, user_id):
    answers = Answer.objects.filter(user_id=user_id)
    departments = Department.objects.all()

    user = User.objects.get(id=user_id)

    header = f'All questions of {user.name()}'
    title = f'{user.first_name}\'s Questions'

    logged_in_user = User.objects.get(id=request.session['user_id'])

    return render(request, 'users/user-answers.html', {
        'answers': answers,
        'departments': departments,
        'header': header,
        'title': title,
        'user': user,
        'logged_in_user': logged_in_user,
        'questions_upvoted': logged_in_user.question_upvotes(),
        'questions_downvoted': logged_in_user.question_downvotes(),
    })
