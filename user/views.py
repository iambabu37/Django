from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.serializers import ModelSerializer, EmailField, CharField, ValidationError
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserProfileForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views import View
from .forms import SignupForm, LoginForm
from rest_framework_simplejwt.tokens import RefreshToken

CustomUser = get_user_model()


class SignUpSerializer(ModelSerializer):
    email = EmailField(required=True)
    password = CharField(write_only=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password')

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise ValidationError("Email is already in use.")
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "my_app/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass email prefix to template (before @)
        user_email = self.request.user.email or ""
        emailprefix = user_email.split('@')[0] if '@' in user_email else self.request.user.username
        context['emailprefix'] = emailprefix
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserProfileForm
    template_name = "my_app/profile_update.html"
    success_url = reverse_lazy('profile')

    def get_object(self):
        # Return logged-in user object to update
        return self.request.user
    
class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'my_app/signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'my_app/signup.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'my_app/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            refresh = RefreshToken.for_user(user)
            print(refresh)
            response = redirect('home')
            response.set_cookie('access_token', str(refresh.access_token), httponly=True)
            response.set_cookie('refresh_token', str(refresh), httponly=True)
            return response

        return render(request, 'my_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    response = redirect('login')
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
    return response

class HomeView(View):
    def get(self, request):
        return render(request, 'my_app/home.html')

def profile(request):
    user = request.user
    email_username = user.email.split("@")[0] if user.email else user.username
    content = {'user':user,'emailprefix':email_username}
    return render(request,'my_app/profile.html',content)