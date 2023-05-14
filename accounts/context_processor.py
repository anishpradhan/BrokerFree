from .forms import LoginForm, RegisterForm

def inject_form(request):
    return {'signin_form': LoginForm(), 'register_form': RegisterForm()}