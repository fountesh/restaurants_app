from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm

class UserRegistrationView(CreateView):
   form_class = CustomUserCreationForm
   template_name = 'users/siginup.html'
   success_url = reverse_lazy('login')

   def form_valid(self, form):
       response = super().form_valid(form)
       messages.success(self.request, 'Account created successfully! Please login.')
       return response

class UserLoginView(LoginView):
   template_name = 'users/login.html'
   redirect_authenticated_user = True
   
   def get_success_url(self):
       return reverse_lazy('home')
   
   def form_valid(self, form):
       messages.success(self.request, f'Welcome back, {form.get_user().username}!')
       return super().form_valid(form)

class UserLogoutView(LogoutView):
   next_page = 'login'

   def dispatch(self, request, *args, **kwargs):
       messages.info(request, 'You have been logged out.')
       return super().dispatch(request, *args, **kwargs)

class UserProfileView(LoginRequiredMixin, UpdateView):
   form_class = CustomUserChangeForm
   template_name = 'users/profile.html'
   success_url = reverse_lazy('profile')
   
   def get_object(self):
       return self.request.user
   
   def form_valid(self, form):
       messages.success(self.request, 'Your profile has been updated!')
       return super().form_valid(form)

   def form_invalid(self, form):
       messages.error(self.request, 'Please correct the errors below.')
       return super().form_invalid(form)