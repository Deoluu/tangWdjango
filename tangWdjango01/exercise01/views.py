from django import http
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Exercise 01! <br> <a href='/exercise01/about/'> About </a>")

def about(request):
    return HttpResponse("Rango says here is the about page! <br> <a href='/exercise01/'> Home <a>")