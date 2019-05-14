from django.urls import path
from . import views

# questions urls

urlpatterns = [
    path('<int:question_id>/', views.question, name='question'),
    path('question-vote/', views.question_vote, name='question-vote'),
    path('answer-vote/', views.answer_vote, name='answer-vote')
]
