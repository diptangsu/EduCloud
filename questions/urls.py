from django.urls import path
from . import views

# questions urls

urlpatterns = [
    path('<int:question_id>/', views.question, name='question')
]
