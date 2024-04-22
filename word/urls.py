from django.urls import path
from . import views

urlpatterns = [
    path('delete_word/<int:word_id>/', views.delete_word, name='delete_word'),
]
