from django.http.response import HttpResponse
from django.shortcuts import render


def registerUser(request):
    return HttpResponse('This is our reg Form')