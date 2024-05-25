from django.urls import path

from . import views

urlpatterns = [
    path('view_languages/', views.view_languages, name='view_languages'),
    path('create_language/', views.create_language, name='create_language'),
    path('edit_language/<int:language_id>/', views.edit_language, name='edit_language'),
    path('delete_language/<int:language_id>/', views.delete_language, name='delete_language')
]
