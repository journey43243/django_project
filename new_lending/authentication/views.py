from typing import Any
import datetime
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.middleware import get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, DetailView, TemplateView, ListView
from django.core.mail import send_mail
from .forms import Authentication, Regist, ResetPasswordForm, ResetPasswordConfirmForm
from new_lending import settings
from django import utils

from lending.models import usersOrders


class Authenticate(LoginView):
    form_model = Authentication
    template_name = 'authentication.html'


class Profile(LoginRequiredMixin,ListView):
    template_name = 'profile.html'
    model = get_user_model()
    context_object_name = 'orders'

    def get_queryset(self):
        return usersOrders.objects.filter(userLogin_id = get_user(self.request).id)


class Registration(FormView):
    template_name = 'registration.html'
    form_class = Regist

    # def get_success_url(self):
    #     return reverse_lazy('authentication:login')

    def form_valid(self, form):
        form.save(commit = False)
        return redirect('authentication:login')



class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('authentication:login')


class ResetPassword(FormView):
    form_class = ResetPasswordForm
    template_name = 'pass_reset.html'

    def form_valid(self, form):
        url = get_user_model().get_password_reset_url(get_user_model().objects.get(email = form.cleaned_data['email']))
        send_mail("Reset password", f"Join to url to reset your password\n{url}", settings.EMAIL_HOST_USER, [form.cleaned_data['email']])
        time_success = datetime.datetime.now() + datetime.timedelta(minutes=5)
        return render(self.request, 'reset_send.html')


class ResetPasswordConfirm(FormView):
    template_name = 'password_reset_confirm.html'
    form_class = ResetPasswordConfirmForm

    def form_valid(self, form):
        user_id = utils.http.urlsafe_base64_decode(self.kwargs['uidb64'])#self.kwargs['uidb64'].
        user = get_user_model().objects.get(id = user_id)
        user.set_password(form.cleaned_data['password2'])
        user.save()
        return redirect('authentication:login')