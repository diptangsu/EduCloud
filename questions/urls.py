from django.urls import path
from . import views

# questions urls

urlpatterns = [
    path('all-questions/', views.all_questions, name='all-questions'),
    path('<int:question_id>/', views.question, name='question'),
    path('question-vote/', views.question_vote, name='question-vote'),
    path('answer-vote/', views.answer_vote, name='answer-vote'),
    path('ask-question/', views.ask_question, name='ask-question'),
    path('search-question/', views.search, name='search-question')
]
