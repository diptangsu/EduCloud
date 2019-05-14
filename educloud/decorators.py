from functools import wraps

from django.shortcuts import redirect
from django.contrib import messages


def login_required(func):
    wraps(func)

    def check(request, *args, **kwargs):
        if 'user_id' in request.session:
            return func(request, *args, **kwargs)
        else:
            messages.add_message(request, messages.ERROR, 'Please login to access this page')
            return redirect('user-login')

    return check
