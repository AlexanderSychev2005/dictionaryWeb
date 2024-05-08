from django.shortcuts import render, redirect

from language.models import Language
from .forms import LanguageForm, LanguageEditForm


# Create your views here.
def view_languages(request):
    languages = Language.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        languages = languages.filter(name__icontains=search_query)
    return render(request, 'language/view_languages.html',
                  {'languages': languages})


def create_language(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('language:view_languages')
    form = LanguageForm()
    return render(request, 'language/create_language.html', {'form': form})


def edit_language(request, language_id):
    language = Language.get_by_id(language_id)
    if request.method == 'POST':
        form = LanguageEditForm(request.POST, instance=language)
        if form.is_valid():
            form.save()
            return redirect('language:view_languages')
    form = LanguageEditForm(instance=language)
    return render(request, 'language/edit_language.html', {'form': form})


def delete_language(request, language_id):
    if request.method == 'POST':
        Language.delete_by_id(language_id)
        return redirect('language:view_languages')
    return render(request, 'language/delete_language.html')
