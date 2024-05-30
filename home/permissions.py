from django.shortcuts import redirect

def has_view_perm(func):
    def wrapper(request,*args, **kwargs):
        if request.user.is_anonymous:
            return redirect('login:login')
        return func(request, *args, **kwargs)  
    return wrapper 
def has_edit_perm(func):
    def wrapper(request,*args, **kwargs):
        if request.user.is_staff:
           return func(request, *args, **kwargs)  
        if  request.user.role.type!='Admin' :
            return redirect('login:login')
        return func(request, *args, **kwargs)  
    return wrapper

def has_create_perm(func):
    def wrapper(request,*args, **kwargs):
        if request.user.is_staff:
           return func(request, *args, **kwargs)  
        print(request.user.role.type)
        if  request.user.role.type!='Admin' and request.user.role.type!='Developer':
            return redirect('login:login')
        return func(request, *args, **kwargs)  
    return wrapper

def has_delete_perm(func):
    def wrapper(request,*args, **kwargs):
        if request.user.is_staff:
           return func(request, *args, **kwargs)  
        if  request.user.role.type!='Admin' :
            return redirect('login:login')
        return func(request, *args, **kwargs)  
    return wrapper