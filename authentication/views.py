from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from .forms import UserLoginForm, UserRegistrationForm, ProfileUserForm, PasswordChangeForm
from django.contrib import messages
from dictionary.models import Dictionary
from language.models import Language


# Create your views here.
@login_required
def index_view(request):
    source_language = request.GET.get("source_language", "")
    target_language = request.GET.get("target_language", "")

    if source_language and target_language:
        source_language_id = Language.get_by_name(source_language).id
        target_language_id = Language.get_by_name(target_language).id
        dictionaries = Dictionary.objects.filter(source_language_id=source_language_id,
                                                 target_language_id=target_language_id)
    if source_language:
        source_language_id = Language.get_by_name(source_language).id
        dictionaries = Dictionary.objects.filter(source_language_id=source_language_id)
    elif target_language:
        target_language_id = Language.get_by_name(target_language).id
        dictionaries = Dictionary.objects.filter(target_language_id=target_language_id)
    else:
        dictionaries = Dictionary.get_all()

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


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("authentication:login"))


def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                messages.success(request, 'Registration was successful!')
                return redirect("authentication:login")

    else:
        form = UserRegistrationForm()
    return render(request, "authentication/registration.html", {'form': form})


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'authentication/profile.html'

    # extra_context = {'title': 'Profile'}

    def get_success_url(self):
        return reverse_lazy('authentication:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("authentication:password_change_done")
    template_name = 'authentication/password_change_form.html'
