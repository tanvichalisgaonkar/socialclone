from django.url import path,re_path
from django.contrib.auth import views as auth_views
from .import views

app_name ='accounts'

urlpatterns =[
	re_path(r'login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
	
]