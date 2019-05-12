from django.contrib import admin

from .models import *

admin.site.register(Question)
admin.site.register(QuestionImage)
admin.site.register(QuestionVote)
admin.site.register(Answer)
admin.site.register(AnswerImage)
admin.site.register(AnswerVote)
