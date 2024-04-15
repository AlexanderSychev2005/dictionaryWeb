from django.shortcuts import render
from .models import Dictionary


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
