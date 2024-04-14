from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib import messages


# Create your views here.
@login_required
def index_view(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse("authentication:login"))
    return render(request, "authentication/index.html")


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd["email"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    messages.error(request, "Disabled account")
                    return render(request, "authentication/login.html", {
                        'form': form
                    })
            else:
                messages.error(request, "Incorrect email or password")
                return render(request, "authentication/login.html", {
                    'form': form
                })

    else:
        form = UserLoginForm()
    return render(request, "authentication/login.html", {'form': form})
