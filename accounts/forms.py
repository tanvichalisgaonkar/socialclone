from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django import forms


class UserCreateForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	print('reach forms')
	class Meta():
		model = User
		fields = ('username','email','password','password')
		

	def __init__(self,*args,**kwargs): 
		super().__init__(*args,**kwargs)
		self.fields['username'].label = "User Name"
		self.fields['email'].label = "Email Address"
		self.fields['password'].label = "Confirm Password"
		