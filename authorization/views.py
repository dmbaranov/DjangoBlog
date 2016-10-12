from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View

from .form import RegistrationForm
from .models import AppUser


class RegistrationView(View):
    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            is_login_used = AppUser.objects.filter(username=request.POST['login'])

            if is_login_used:
                messages.add_message(request, messages.ERROR, "This username is in use already")
            else:
                user = AppUser.objects.create_user(request.POST['login'])
                user.set_password(request.POST['password'])
                user.save()

                messages.add_message(request, messages.SUCCESS, "Registration completed successfully!")

        return HttpResponseRedirect(reverse('authorization:result'))

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()

        return render(request, 'authorization/registration.html', {
            'form': form
        })


class LoginView(View):
    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST['login'], password=request.POST['password'])

        if user is not None:
            login(request, user)
        else:
            print("Account doesn't exists!")

        return HttpResponseRedirect(reverse('blog:index'))

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        messages.add_message(request, messages.INFO, request.GET.get('next'))

        return render(request, 'authorization/login.html', {
            'form': form
        })


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)

        return HttpResponseRedirect(reverse('blog:index'))


class AuthResultView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'authorization/auth_result.html')


class ShowUser(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'authorization/profile.html')
