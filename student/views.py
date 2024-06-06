from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome Home.")
def register(request):
    return HttpResponse("Register Here")

# Create your views here.
