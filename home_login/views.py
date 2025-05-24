from django.shortcuts import render
from django.http import HttpResponse
from .forms import login_cliente


# Create your views here.
def login(request):
    # renderiza os dados do formulario de login
    if request.method == 'GET':
        # chama o formulario de login
        form = login_cliente()
        # retorna a requisição do documento html e também os inputs do formulario citado acima
        return render(request, 'login_us.html', {'form': form})
    # o else será para um metodo de recebimento de dados

