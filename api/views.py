from django.http import JsonResponse
from django.shortcuts import render

def api_hello(request):
    return JsonResponse({"message": "Hello World"})

def hello_page(request):
    return render(request, "api/hello.html", {"who": None})

def hello_personal(request, who):
    return render(request, "api/hello.html", {"who": who})

def about_travis(request):
    return render(request, "api/about.html")