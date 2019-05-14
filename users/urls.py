from django.urls import path
from . import views

# users urls

urlpatterns = [
    path('login/', views.login, name='user-login'),
    path('logout/', views.logout, name='user-logout'),
    path('register/', views.register, name='user-register'),
    path('student-register/<int:user_id>', views.student_register, name='student-register'),
    path('professor-register/<int:user_id>', views.professor_register, name='professor-register'),
    path('profile/<int:user_id>/', views.user_profile, name='user-profile'),
    path('questions/<int:user_id>/', views.user_questions, name='user-questions'),
    path('answers/<int:user_id>/', views.user_answers, name='user-answers'),
]
