from django.urls import path, include
from . import views

urlpatterns = [
    path("dict/<int:dict_id>/", views.view_dict, name="view_dict"),

]