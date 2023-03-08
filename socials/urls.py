from django.urls import path
from . import views
urlpatterns = [
    path("", views.socials_index, name="socials_index"),
]