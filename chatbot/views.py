from django.shortcuts import render
from django.shortcuts import Http404
from django.shortcuts import redirect

from academics.models import Department
from users.models import User
from .models import Message, Reply

from educloud.decorators import login_required


@login_required
def chat(request):
    logged_in_user = User.objects.get(id=request.session['user_id'])

    if request.method == 'GET':
        departments = Department.objects.all()

        last_message = Message.objects.filter(user=logged_in_user).last()
        reply = ''
        if last_message is not None:
            try:
                reply = Reply.objects.get(message_id=last_message.id)
                reply = reply.reply
            except Reply.DoesNotExist:
                reply = ''

            last_message = last_message.message
        else:
            last_message = ''

        return render(request, 'chatbot/chat.html', {
            'departments': departments,
            'logged_in_user': logged_in_user,
            'message': last_message,
            'reply': reply,
            'chat': True
        })
    elif request.method == 'POST':
        message_text = request.POST.get('message', None)
        msg = Message()
        msg.user = logged_in_user
        msg.message = message_text
        msg.save()

        return redirect('chat')
    else:
        raise Http404
