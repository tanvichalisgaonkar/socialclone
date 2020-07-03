from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class UserCrearteForm(User):

	class Meta:
		fields = ('username','email','password','password')
		model = get_user_model()

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['username'].label = "Display Name"
		self.fields['email'].label = "Email Address"
		