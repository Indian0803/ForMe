from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('adviser_list')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

def adviser_allowed(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_adviser:
            return redirect('adviser_list')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func