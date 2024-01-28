from django.shortcuts import redirect


def not_logged_in_required(view_function):
    def wrapper(request, *args, **kwarsg):
        if request.user.is_authenticated:
            return redirect('home2')
        else:
            return view_function(request, *args, **kwarsg)

    return wrapper
