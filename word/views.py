from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
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
