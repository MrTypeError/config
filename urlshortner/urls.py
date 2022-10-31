from django.urls import path
from .views import home, redirectUrl

appname = "urlshortner"

urlpatterns = [
    path("", home, name="home"),
    path("<str:shortUrl>", redirectUrl, name="redirect")
]
