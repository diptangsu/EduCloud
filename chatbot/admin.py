from django.contrib import admin

from .models import Message, Reply

admin.site.register(Message)
admin.site.register(Reply)
