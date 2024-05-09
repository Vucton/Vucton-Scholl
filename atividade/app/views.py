from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa


def update(request):
    pass

def delete(request):
    pass
#create
def delete(request):
    pass


#read
def create(request):
    pass

def list(request):
    pass
#read
def detail(request):
    if request.GET:
        valor = request.GET['q']
        pessoas = Pessoa.objects.all().filter(cpf__contains=valor)
    else:
        pessoas = Pessoa.objects.get(all)
        

    html = "<table>"

    for pessoa in pessoas:
        html += "<tr>"
        html += "<td>"+ str(pessoa.id)+"</td>"
        html += "<td>"+ str(pessoa.cfp)+"</td>"
        html += "<td>"+ pessoa.nome+"</td>"
        html += "<td>"+ str(pessoa.idade)+"</td>"
        html += "</tr>"
        html += "</table>"

        return HttpResponse(html)