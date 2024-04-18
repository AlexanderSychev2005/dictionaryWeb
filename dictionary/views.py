from django.shortcuts import render, redirect
from .models import Dictionary
from .forms import DictionaryForm, DictionaryEditForm
from django.contrib.auth.decorators import user_passes_test


def is_admin_user(user):
    return user.is_admin


# Create your views here.
def view_dict(request, dict_id):
    dictionary = Dictionary.objects.get(pk=dict_id)
    words = dictionary.words.all().order_by('text')

    search_query = request.GET.get('search', '')
    if search_query:
        words = words.filter(text__icontains=search_query)

    return render(request, 'dictionary/view_dict.html',
                  {'dictionary': dictionary,
                   'words': words}
                  )


@user_passes_test(is_admin_user)
def delete_dict(request, dict_id):
    dictionary = Dictionary.objects.get(pk=dict_id)
    if request.method == 'POST':
        dictionary.delete()
        return redirect("authentication:index")
    return render(request, 'dictionary/delete_dict.html')


@user_passes_test(is_admin_user)
def add_dict(request):
    if request.method == 'POST':
        form = DictionaryForm(request.POST)
        if form.is_valid():
            dictionary = form.save()
            return redirect("authentication:index")

    else:
        form = DictionaryForm()
    return render(request, "dictionary/add.html", {
        'form': form
    })


@user_passes_test(is_admin_user)
def edit_dict(request, dict_id):
    dictionary = Dictionary.objects.get(pk=dict_id)
    if request.method == 'POST':
        form = DictionaryEditForm(request.POST, instance=dictionary)
        if form.is_valid():
            form.save()
            return redirect(f'dictionary:view_dict', dict_id=dict_id)

    else:
        form = DictionaryEditForm(instance=dictionary)
    return render(request, 'dictionary/edit.html', {
        'form': form
    })
