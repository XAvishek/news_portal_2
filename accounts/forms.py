from django import forms
from accounts.models import User, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class EmailValidation(forms.EmailField):
    def validate(self, value):
        try:
            User.objects.get(email=value)
            raise forms.ValidationError('Email already exists')
        except User.MultipleObjectsReturned:
            raise forms.ValidationError('Email already exists')
        except User.DoesNotExist:
            pass

class UserSignUpForm(UserCreationForm):
    email = EmailValidation(required=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name',
                    'last_name', 'password1', 'password2']

class UserUpdateForm(UserChangeForm):
    email = forms.EmailField()
    email = EmailValidation(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'dob', 'address']
