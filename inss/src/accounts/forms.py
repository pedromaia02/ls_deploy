from django.contrib.auth import (
		authenticate,
		get_user_model,
		login,
		logout,
		)

from django import forms


class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("Usuario ou senha incorretos")
			if not user.check_password(password):
				raise forms.ValidationError("Usuario ou senha incorretos")
			if not user.is_active:
				raise forms.ValidationError("Este usuario esta desativado")
		return super(UserLoginForm, self).clean(*args, **kwargs)

		# user_qs = User.objects.filter(username=username)
		# if user_qs.count() == 1:
		#     user = user_qs.first()
