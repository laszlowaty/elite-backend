from django.shortcuts import render
import requests

base_url = "http://127.0.0.1:8000/"

# Create your views here.
def index(request):
    station = requests.get(base_url+"stations/15/").json()
    content = []
    for key, value in station.items():
        content.append((key, value))
    return render(request, "base.html", {"content":content})
