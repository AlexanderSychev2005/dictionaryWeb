from django.shortcuts import render, redirect
from .models import Dictionary
from .forms import DictionaryForm


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


def delete_dict(request, dict_id):
    dictionary = Dictionary.objects.get(pk=dict_id)
    if request.method == 'POST':
        dictionary.delete()
        return redirect("authentication:index")
    return render(request, 'dictionary/delete_dict.html')


def add(request):
    if request.method == 'POST':
        form = DictionaryForm(request.POST)
        if form.is_valid():
            dictionary = form.save()
            return redirect("authentication:index")

    else:
        form = DictionaryForm()
    return render(request, "dictionary/add.html", {
        "form": form
    })
