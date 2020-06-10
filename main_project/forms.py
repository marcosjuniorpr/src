from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUser(UserCreationForm):

	username = forms.CharField(widget=forms.TextInput())
	first_name = forms.CharField(widget=forms.TextInput())
	last_name = forms.CharField(widget=forms.TextInput())
	password1 = forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(widget=forms.PasswordInput())
	email = forms.CharField(widget=forms.EmailInput())

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2' , 'email', \
						'first_name', 'last_name')


	def clean(self,*args,**kwargs):

		"""
		To check the new email added by the
		user is already exist or not. If already
		exist than that email can't be used
		"""

		email_qs = User.objects.filter(email = self.cleaned_data.get('email'))

		if email_qs.exists():
			raise forms.ValidationError("This email has already been registered")

		return super(RegisterUser,self).clean(*args,**kwargs)
		



