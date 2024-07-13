from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Pessoa
from django.db.models import Q
from app.forms import PessoaForm


def delete(request):
    pass

def create(request):
    pass
def update(request):
    pass

def add(request):
    if request.method == "POST":
        form = PessoaForm(request.POST)

        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/list/')
    else:
        form = PessoaForm()

    return render(request, "pessoa/add.html", {"form": form})


def list(request):

    obj = request.GET.get('obj')
    if obj:
        pessoas = Pessoa.objects.filter(
            Q(nome__icontains=obj) |
            Q(cpf__contains=obj) |
            Q(id__contains=obj)
            )

    else:
        pessoas = Pessoa.objects.all()
        
    return render(request, "pessoa/index.html", {'pessoas':pessoas})

def detail(request, pessoa_id):
    pessoa = Pessoa.objects.get(pk=pessoa_id)

    return render(request, "pessoa/detalhes.html",{'pessoa': pessoa} )