from django.urls import path
from . import views

# chatbot urls

urlpatterns = [
    path('', views.chat, name='chat')
]
