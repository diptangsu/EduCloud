from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import Http404
from django.shortcuts import redirect

from .models import Question
from .models import Answer

from academics.models import Department


def home(request):
    departments = Department.objects.all()

    return render(request, 'questions/home.html', {
        'departments': departments
    })


def questions(request):
    all_questions = Question.objects.all().order_by('-timestamp')[:20]
    return render(request, 'questions/all-questions.html', {
        'all_questions': all_questions
    })


def question(request, question_id):
    if request.method == 'GET':
        this_question = get_object_or_404(Question, id=question_id)
        user = this_question.user
        answers = Answer.objects.filter(question_id=question_id).order_by('timestamp')
        answers_sorted = sorted(answers.all(), key=lambda a: a.votes(), reverse=True)

        return render(request, 'questions/question.html', {
            'this_question': this_question,
            'user': user,
            'answers': answers_sorted
        })
    elif request.method == 'POST':
        # fetch answer details
        # save answer
        return redirect(f'/question/{question_id}')
    else:
        raise Http404
