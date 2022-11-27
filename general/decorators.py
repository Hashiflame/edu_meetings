from functools import wraps
from django.http import HttpResponseRedirect


def authors_only(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        user = request.user
        if hasattr(user, 'mentor'):
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
    return wrap


def login_forbidden(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
    return wrap
