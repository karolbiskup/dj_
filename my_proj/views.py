from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Zaczynam tworzenie stron w programie django to jest moja pierwsza strona w django")
