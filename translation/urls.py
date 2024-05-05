from django.urls import path
from . import views

urlpatterns = [
    path(r'create_translation/<int:word_id>/', views.create_translation, name='create_translation')
]