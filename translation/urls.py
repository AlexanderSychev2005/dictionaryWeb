from django.urls import path
from . import views

urlpatterns = [
    path('create_translation/<int:word_id>/', views.create_translation, name='create_translation'),
    path('update_translation/<int:translation_id>/', views.update_translation, name='update_translation'),
    path('delete_translation/<int:translation_id>/', views.delete_translation, name='delete_translation')
]