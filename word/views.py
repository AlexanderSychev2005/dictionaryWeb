from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import WordForm, WordEditForm
from .models import Word


# Create your views here.
def is_admin_user(user):
    return user.is_admin


@user_passes_test(is_admin_user)
def delete_word(request, word_id):
    word = Word.objects.get(id=word_id)
    if request.method == 'POST':
        word.delete()
        return redirect("authentication:index")
    return render(request, 'word/delete.html')


@user_passes_test(is_admin_user)
def create_word(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.save()
            return redirect("/")
    form = WordForm()
    return render(request, 'word/create_word.html',
                  {'form': form})


@user_passes_test(is_admin_user)
def update_word(request, word_id):
    word = Word.objects.get(id=word_id)
    if request.method == 'POST':
        form = WordForm(request.POST, instance=word)
        if form.is_valid():
            word = form.save()
            return redirect("/")
    form = WordForm(instance=word)
    return render(request, 'word/edit_word.html',
                  {'form': form})

