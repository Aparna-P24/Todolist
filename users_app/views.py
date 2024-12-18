from django.shortcuts import render, redirect
from users_app.forms import CustomCreationForm
from django.contrib import messages
from django.contrib.auth import logout


def register(request):
    if request.method == "POST":
        register_form = CustomCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(
                request, "New user registered! Login to Get Started!!")
            return redirect('register')
    else:
        register_form = CustomCreationForm()
        return render(
            request, 'register.html', {
                'register_form': register_form})


def custom_logout(request):
    logout(request)
    return redirect('login')