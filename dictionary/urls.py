from django.urls import path, include
from . import views

urlpatterns = [
    path("dict/<int:dict_id>/", views.view_dict, name="view_dict"),
    path("delete_dict/<int:dict_id>, views.delete_dict", views.delete_dict, name="delete_dict"),
    path("add_dict/", views.add, name="add_dict"),

]