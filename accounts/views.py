from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserCreateForm
from django.contrib.auth.models import User
# Create your views here.

class SignUp(CreateView):
	print('reach veiws')
	form_class = UserCreateForm
	success_url = reverse_lazy('login')
	template_name = 'accounts/signup.html'
