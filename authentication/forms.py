from django import forms
from django.contrib.auth.forms import UserCreationForm
from authentication.models import UserProfile, User


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(attrs={'placeholder': "Username"}),
            "email": forms.EmailInput(attrs={'placeholder': " Email"}),
            "password1": forms.PasswordInput(attrs={'placeholder': "Enter password"}),
            "password2": forms.PasswordInput(attrs={'placeholder': "Confirm password"}),
        }

class UserProfileForm(forms.ModelForm):

    profile_img = forms.ImageField(widget=forms.FileInput)
    cover_img = forms.ImageField(widget=forms.FileInput)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name", "profile_img", "cover_img", "date_of_birth", "address_line1", "address_line2", "city", "nationality", "zipcode", "mobile_num"]

        widgets = {
            "first_name": forms.TextInput(attrs={'placeholder': "First name"}),
            "last_name": forms.TextInput(attrs={'placeholder': "Last name"}),
            "address_line1": forms.TextInput(attrs={'placeholder': "Address Detail 1"}),
            "address_line2": forms.TextInput(attrs={'placeholder': "Address Detail 2"}),
            "city": forms.TextInput(attrs={'placeholder': "City or state"}),
            "nationality": forms.TextInput(attrs={'placeholder': "Nationality"}),
            "zipcode": forms.TextInput(attrs={'placeholder': "Zipcode"}),
            "mobile_num": forms.TextInput(attrs={'placeholder': "Phone or moblie number"}),
        }
