from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

# Create your views here.

class UserRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users\siginup.html'
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        return super().form_valid(form)

class UserLogoutView(LogoutView):
    template_name = 'users\login.html'

class UserProfileView(TemplateView):
    template_name = 'users\profile.html'