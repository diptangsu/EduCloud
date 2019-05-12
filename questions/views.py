from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import Http404
from django.shortcuts import redirect

from .models import Question
from .models import Answer
from .models import AnswerVote

from collections import namedtuple


def questions(request):
    all_questions = Question.objects.all().order_by('timestamp')
    return render(request, 'questions/all-questions.html', {
        'all_questions': all_questions
    })


def question(request, question_id):
    if request.method == 'GET':
        this_question = get_object_or_404(Question, id=question_id)
        user = this_question.user
        answers = Answer.objects.filter(question_id=question_id)

        AnswerData = namedtuple('AnswerData', 'answer_user body votes timestamp')
        answers_list = []

        for answer in answers:
            answer_user = answer.user
            answer_upvotes = AnswerVote.objects.filter(answer=answer, vote_type='U').count()
            answer_downvotes = AnswerVote.objects.filter(answer=answer, vote_type='D').count()
            votes = answer_upvotes - answer_downvotes

            answers_list.append(AnswerData(
                answer_user=answer_user,
                body=answer.body,
                votes=votes,
                timestamp=answer.timestamp
            ))

        answers_list.sort(key=lambda a: a.votes, reverse=True)

        return render(request, 'questions/question.html', {
            'this_question': this_question,
            'user': user,
            'answers': answers_list
        })
    elif request.method == 'POST':
        # fetch answer details
        # save answer
        return redirect(f'/question/{question_id}')
    else:
        raise Http404
