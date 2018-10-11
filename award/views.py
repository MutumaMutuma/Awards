from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt

# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')

def index(request):
    date = dt.date.today()
    return render(request, 'all-posts/index.html', {"date": date,})