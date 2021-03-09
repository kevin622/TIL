from django.shortcuts import render
from django.http.response import HttpResponse
import random

# Create your views here.
def index(request):
    lotto = random.sample(range(1, 46), 6)
    return HttpResponse(f'Pick: {sorted(lotto)}')