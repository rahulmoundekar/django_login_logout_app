from django import forms

from user_login_logout.models import User, LoginUser


class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=45,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control form-control-user', 'placeholder': 'Enter Email'}))
    password = forms.CharField(max_length=45,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control form-control-user', 'placeholder': 'Enter Password'}))

    class Meta:
        model = User
        fields = '__all__'


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = LoginUser
        fields = '__all__'
