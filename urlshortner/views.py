from django.shortcuts import render
from django.http import HttpResponse 
from .models import Shortner
from .forms import ShortnerFrom
# Create your views here.

def home(request):
    tmplt = "home.html"
    context = {}
    return render(request, tmplt, context)
