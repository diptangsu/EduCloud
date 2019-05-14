from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import Http404
from django.shortcuts import redirect

from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse

from .models import Question
from .models import Answer
from .models import QuestionVote
from .models import AnswerVote

from academics.models import Department
from users.models import User

import json
from educloud.decorators import login_required


@login_required
def all_questions(request):
    questions = Question.objects.all().order_by('-timestamp')[:20]
    departments = Department.objects.all()

    header = 'All Questions'

    return render(request, 'questions/questions.html', {
        'questions': questions,
        'departments': departments,
        'header': header,
        'title': header
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


@csrf_exempt
def question_vote(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id', -1)

        data = json.loads(request.body.decode('utf-8'))

        question_id = data.get('question_id', -1)
        vote_type = data.get('vote_type', 'NA')

        try:
            ques = Question.objects.get(id=question_id)
            user = User.objects.get(id=user_id)

            vote = QuestionVote()
            vote.question = ques
            vote.user = user
            vote.vote_type = vote_type

            vote.save()
        except Question.DoesNotExist:
            pass
        except User.DoesNotExist:
            pass

        ques = Question.objects.get(id=question_id)
        votes = ques.votes()

        return JsonResponse({'votes': votes})
    else:
        raise Http404


@csrf_exempt
def answer_vote(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id', -1)

        data = json.loads(request.body.decode('utf-8'))

        answer_id = data.get('question_id', -1)
        vote_type = data.get('vote_type', 'NA')

        vote = AnswerVote()
        vote.question_id = answer_id
        vote.user_id = user_id
        vote.vote_type = vote_type

        vote.save()

        ans = Answer.objects.get(id=answer_id)
        votes = ans.votes()

        return JsonResponse({'votes': votes})
    else:
        raise Http404


def ask_question(request):
    if request.method == 'GET':
        return render(request, 'questions/ask-question.html')
    elif request.method == 'POST':
        pass
    else:
        raise Http404
