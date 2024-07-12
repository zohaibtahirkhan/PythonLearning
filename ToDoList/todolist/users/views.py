from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = UserForm()
    return render(request, 'register.html', context={"form": form})


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'logout.html')

