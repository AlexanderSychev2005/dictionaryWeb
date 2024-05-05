from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect

from translation.forms import TranslationForm
from word.models import Word


# Create your views here.
def is_admin_user(user):
    return user.is_admin


@user_passes_test(is_admin_user)
def create_translation(request, word_id):
    word = Word.objects.get(id=word_id)
    if request.method == 'POST':
        form = TranslationForm(request.POST, word_id=word_id)
        if form.is_valid():
            translation = form.save()
            word.translations.add(translation)
            return redirect('word:view_word', word_id=word_id)
    else:
        form = TranslationForm(word_id=word_id)
        return render(request, 'translation/create_translation.html',
                      {'form': form})
