from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def login(request):
    nome = 'lucas'
    return render(request, 'login_us.html', {'nome': nome})