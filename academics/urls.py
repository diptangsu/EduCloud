from django.urls import path
from . import views

# academics urls

urlpatterns = [
    path('questions/<str:dept>/', views.questions, name='department-question'),
    path('professors/<str:dept>/', views.professors, name='department-professors')
]
