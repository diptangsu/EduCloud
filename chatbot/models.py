from django.db import models

from users.models import User


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.TextField()

    def __str__(self):
        return f'({self.id}) {self.user.name()}: {self.message}'


class Reply(models.Model):
    message = models.OneToOneField(Message, on_delete=models.CASCADE, null=True)
    reply = models.TextField()

    def __str__(self):
        return f'({self.id}) {self.message.message}: {self.reply}'
