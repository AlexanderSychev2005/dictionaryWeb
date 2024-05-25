from django.urls import path
from . import views

urlpatterns = [
    path("dict/<int:dict_id>/", views.view_dict, name="view_dict"),
    path("delete_dict/<int:dict_id>/", views.delete_dict, name="delete_dict"),
    path("add_dict/", views.add_dict, name="add_dict"),
    path("edit_dict/<int:dict_id>/", views.edit_dict, name="edit_dict")
]
