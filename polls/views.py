from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello ,Lunatic Prince.")

def princess(request):
    return HttpResponse("You are my Princess , sona",1)
