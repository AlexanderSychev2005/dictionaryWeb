from django.urls import path

from . import views

urlpatterns = [
    path('delete_word/<int:word_id>/', views.delete_word, name='delete_word'),
    path('create_word/<int:dictionary_id>', views.create_word, name='create_word'),
    path('update_word/<int:word_id>/', views.update_word, name='update_word'),
    path('word/<int:word_id>/', views.view_word, name='view_word')

]
