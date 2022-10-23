from django.urls import path
from .views import home

appname = "urlshortner"

urlpatterns = [
    path("", home, name = "home")
]