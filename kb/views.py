from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles


def home(request):
    # # return HttpResponse("<h1>Knowledge base - homepage</h1>")
    # articles = [
    #     {
    #         "author": "John Doe",
    #         "title": "How to start development server",
    #         "content": "python manage.py runserver",
    #         "date": "December 4, 2021"
    #     },
    #     {
    #         "author": "Max Doe",
    #         "title": "How to stop development server",
    #         "content": "Ctrl C",
    #         "date": "Januar 4, 2023"
    #     }
    # ]
    context = {"title": "Articles", "articles": Articles.objects.all()}
    return render(request, "kb/home.html", context)


def about(request):
    # return HttpResponse("<h1> About knowledge base</h1>")
    context = {"title": "About page"}
    return render(request, "kb/about.html", context)
