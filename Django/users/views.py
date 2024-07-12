from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.messages import success
from .forms import UserRegistrationForm, ProfileUpdateForm, UserUpdateForm


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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            success(request, "Your Account has been updated!")
            return redirect('blog-home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profile.html', context={"u_form": u_form, "p_form": p_form})

