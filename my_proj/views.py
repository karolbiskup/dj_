from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("Zaczynam tworzenie stron w django to jest moja strona po drobnych modyfikacjach")


def caption_1(request):
    return HttpResponse('Zaczynam tworzenie stron w django to jest moj drugi napis')

