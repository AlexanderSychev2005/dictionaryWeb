from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

from dictionary.models import Dictionary
from .forms import WordForm
from .models import Word


# Create your views here.
def is_admin_user(user):
    return user.is_admin


@user_passes_test(is_admin_user)
def delete_word(request, word_id):
    if request.method == 'POST':
        Word.delete_by_id(word_id)
        return redirect("authentication:index")
    return render(request, 'word/delete.html')


@user_passes_test(is_admin_user)
def create_word(request, dictionary_id):
    dictionary = Dictionary.get_by_id(dictionary_id)
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.save()
            dictionary.words.add(word)
            return redirect("dictionary:view_dict", dict_id=dictionary.id)
    else:
        form = WordForm()
        return render(request, 'word/create_word.html',
                      {'form': form})


@user_passes_test(is_admin_user)
def update_word(request, word_id):
    word = Word.get_by_id(word_id)

    if request.method == 'POST':
        form = WordForm(request.POST, instance=word)
        if form.is_valid():
            form.save()
            return redirect('word:view_word', word_id=word_id)

    form = WordForm(instance=word)
    return render(request, 'word/edit_word.html',
                  {'form': form})


def view_word(request, word_id):
    request_query = request.GET.get('search', '')
    word = Word.get_by_id(word_id)
    translations = word.translations.filter(text__icontains=request_query)
    return render(request, 'word/view_word.html',
                  {'word': word,
                   'translations': translations})
