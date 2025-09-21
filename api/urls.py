from django.urls import path
from .views import api_hello, hello_page, hello_personal, about_travis

urlpatterns = [
    path("api/", api_hello, name="api-hello"),
    path("hello/", hello_page, name="hello-page"),
    path("hello/<str:who>/", hello_personal, name="hello-personal"),
    path("travis-lester/", about_travis, name="travis-lester"),
]
