from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm, UserProfileForm
from .models import User

def register(request):
    userform = SignupForm()
    profileform = UserProfileForm()
    if request.method == "POST":
        userform = SignupForm(request.POST)
        profileform = UserProfileForm(request.POST, request.FILES)

        if userform.is_valid() and profileform.is_valid():
            new_user = userform.save()
            profile = profileform.save(commit=False)
            profile.user = new_user
            profile.save()

            messages.success(request, "Your account has been created successfully!")
        else:
            return redirect('signup')

    context = {
        "userform" : userform,
        "profileform" : profileform,
    }

    return render(request, "authentication/signup.html", context)
