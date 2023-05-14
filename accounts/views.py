from django.shortcuts import redirect, HttpResponseRedirect, reverse, render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.translation import gettext_lazy as _

from .forms import LoginForm, RegisterForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'signin.html'
    redirect_authenticated_user = True


class RegisterView(UserPassesTestMixin, generic.CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'signup-light.html'
    success_url = reverse_lazy('home:home')
    permission_denied_message = _("You are already registered!")

    # def form_valid(self, form):
    #     form.save()
    #     new_user = auth.authenticate(username=form.cleaned_data['username'],
    #                             password=form.cleaned_data['password1'],
    #                             )
    #     auth.login(self.request, new_user)
    #     return HttpResponseRedirect(self.success_url)
      
    def test_func(self):
        return self.request.user.is_anonymous
    
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse("home:home"))

def logout(request):
    auth.logout(request)
    return redirect('home:home')
