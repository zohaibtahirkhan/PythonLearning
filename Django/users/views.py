from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.messages import success
from .forms import UserRegistrationForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            success(request, "User has been created!")
            return redirect('blog-home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', context={"form": form})


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'logout.html')


@login_required
def profile(request):
    return render(request, 'profile.html')

