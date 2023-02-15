from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(Request):
    return render(Request, 'Page_Reg/home.html')
    # return HttpResponse("<h1>Hello..! Welcome to Moment By Moment Photo Gallery.</h1>")
