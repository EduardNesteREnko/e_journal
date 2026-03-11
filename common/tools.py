from functools import wraps

from django.core.exceptions import PermissionDenied

def student(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if not request.user.groups.filter(name='Student').exists():
            raise PermissionDenied
        else:
            return func(request, *args, **kwargs)
    return wrapper