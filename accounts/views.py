from django.shortcuts import render
from django.contrib.auth import login
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CusromuserCreationForm

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    sucess_url = reverse_lazy('accounts:login')
    template_name = "accounts/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect()
