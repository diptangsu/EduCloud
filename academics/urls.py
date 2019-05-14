from django.urls import path
from . import views

# academics urls

urlpatterns = [
    path('department/<str:department>/questions/', views.department_questions, name='department-question'),
    path('subject/<str:subject_code>/questions/', views.subject_questions, name='subject-question'),
    path('professors/<str:department>/', views.department_professors, name='department-professors'),
    path('all-professors/', views.all_professors, name='all-professors'),
]
