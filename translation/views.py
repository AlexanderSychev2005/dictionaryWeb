from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect

from translation.forms import TranslationForm, TranslationEditForm
from translation.models import Translation
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


@user_passes_test(is_admin_user)
def delete_translation(request, translation_id):
    translation = Translation.objects.get(id=translation_id)
    word_id = translation.source_word.id

    if request.method == 'POST':
        translation.delete()
        return redirect("word:view_word", word_id=word_id)
    return render(request, 'translation/delete_translation.html')


@user_passes_test(is_admin_user)
def update_translation(request, translation_id):
    translation = Translation.objects.get(id=translation_id)
    word_id = translation.source_word.id

    if request.method == 'POST':
        form = TranslationEditForm(request.POST, instance=translation)
        translation.delete()
        return redirect("word:view_word", word_id=word_id)
    form = TranslationEditForm(instance=translation)
    return render(request, 'translation/edit_translation.html', {
        "form": form
    })
