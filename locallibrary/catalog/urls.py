from django.urls import path
from . import views # "." is relative import from last package, i.e. path from django.urls

urlpatterns = [
    path("", views.index, name="index"),
]
