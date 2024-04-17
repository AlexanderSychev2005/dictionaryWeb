from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib import messages
from dictionary.models import Dictionary
from language.models import Language
from users.models import CustomUser


# Create your views here.
@login_required
def index_view(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse("authentication:login"))

    source_language = request.GET.get("source_language", "")
    target_language = request.GET.get("target_language", "")

    if source_language and target_language:
        source_language_id = Language.objects.get(name=source_language).id
        target_language_id = Language.objects.get(name=target_language).id
        dictionaries = Dictionary.objects.filter(source_language_id=source_language_id,
                                                 target_language_id=target_language_id)
    if source_language:
        source_language_id = Language.objects.get(name=source_language).id
        dictionaries = Dictionary.objects.filter(source_language_id=source_language_id)
    elif target_language:
        target_language_id = Language.objects.get(name=target_language).id
        dictionaries = Dictionary.objects.filter(target_language_id=target_language_id)
    else:
        dictionaries = Dictionary.objects.all()
    if CustomUser.is_admin_user(request.user):
        return render(request, "authentication/index_admin.html",
                      {"dictionaries": dictionaries})

    return render(request, "authentication/index.html",
                  {"dictionaries": dictionaries})


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
