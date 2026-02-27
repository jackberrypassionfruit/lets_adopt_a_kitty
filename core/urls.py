from django.urls import path

from . import views
from .metrics import inc_request_counter

urlpatterns = [
    path("", inc_request_counter(views.index), name="index"),
]
