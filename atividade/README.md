model responsavel por armazenar os dados no banco]
view responsavel por realizar ações]


o user faz uma requsção para uma url e essa realiza uma ação

passar variavel para uma view
primeiro voce informa isso na url declarando uma variavel dentro da url para receber esse valor. exemplo: ("<int:pessoa_id>", view.app, name="detail")

Agora na view voce tem que informar esse valor que foi armazenado na variavel da url para a funçao da view:

    def detail(request, pessoa_id): ou seja voce criou um parametro para receber a variavel na view

    mas tem um porem que voce precisa converter o valor recebido pelo parametro, como o valor é do tipo inteiro voce
    precisa passar para string ai vc utiliza +str(pessoa_id)+


na url voce pode informa a açao e o valor, ou seja a url é da forma que o programdor deseja, seja a ação primeiro ou o parametro primeiro
    exemplo: path("detail/<int:pessoa_id>", ..., ...) ou path("<int:pessoa_id>/detail/")

#para a prova olhar o diagrama do fluxo do Django
a data da prova mudou por conta do conteudo e vai ter outra atividade


se voce quer usar o model na view voce precisa importar primeiro ele 
    from .models import Pessoa (recapitulando que model é onde fica suas classes)

agora na view na função pessoa
    def list(request):
        voce vai criar uma variavel pessoa que vai receber o model que no caso é a objeto Pessoa
        
        [ aciona o model
        pessoas = Pessoa.objects.all(): aqui estamos armazendo nessa variavel todos os objetos do tipo pessoa que existem no banco de dados.
        nesse momento ele esta recuperando os objetos no banco de dados

        variavel para armazenar o html que sera retornado para o user
        html = "<table>"

        for pessoa in pessoas:
            html += "<tr>"
            html += "<td> + str(pessoa.id) + </td>"
            html += "</tr>"
            html += "</table>

            return a variavel html 

agora será necessario tratar esses dados porque estamos enviando uma resposta html e nao objeto.

quando eu quero chamar uma pessoa na função devo utilizar pk para intender que o parametro que estou recebendo 
é minha primary key do banco de dados da tabela Pessoa
    pessoa = Pessoa.objects.get(pk=pessoa_id)

proximo passo para o nosso sisteminha é listar e busca pessoa especifica

criando um filtro de busca, funçao que seleciona determinado dado

pessoa = Pessoa.objects.all().filter(cpf__contains=query) isso é apenas para string

passar parametro do tipo get fazer uma requisição
implementar a funçao de filter utilizando parametros do tipo get


pegando o parametro passado pelo get
if request.params.GET['q']:
    valor = request.params.GET['q']
    pessoa = Pessoa.objects.all().filter(cpf=valor)

da uma olhada em parametros request Django

Atividade : Fazer um filtro para todos os campos da tabela, ou seja cpf, idade, nome

Na aula de hoje vamos Falar sobre template:

o template nada mais é no django que um html enrriquecido

no django podemos ter um motor para trabalhar com html, ou seja, template enginer.

tem duas formas de utilizar 

{% comandos %}

{{ exibição }}

isso te permite programar dentro do html

vamos gerar um arquivo html em uma pasta e carregar esse arquivo html (loader) para a minha view e passar como parametro
para minha função 

na resposta o template vai pedir um context que seria um dicionario
template.render vc vai precisar renderizar o template que voce armazenou em uma variavel antes
para passalo como respostas do request

lembre-se de importar o loader ou seja From django.templates import loader

BASE__DIR = diretorio base

vamos em configuração e em templates, vamos dizer o caminho de onde o django procurar o templete
ex: DIR[ BASE_DIR /"template]


utilize o atalho de shortcut return render, lembre-se de importar o django.shortcut import render 
para renderizar o template como resposta da funçao





Aula - 28/05

Formularios
para que serve? capitar dados

modelform - vai capiturar o que tem no meu model e gerar um formulario pra vc
ele observa o model e gera o formulario

mas como que usa? 

criar um arquivo form

class meta - dados alem dos dados ( o alem daquilo)

token de formulario csrf, sem esse token voce nao consegue fazer nenhuma ação no django
middleware token

na views add recebe um request .method post
if request.method == post(request.post)
if form.is_valid:
form.save()
ou seja se tudo estiver correto com o formulario ele irar salvar

READ:

criar um arquivo engual ao add.html apague a action

- na url vou adicionar um parametro id como ja foi visto

agora na view
- na def edit renderizar o novo arquivo edit.html

alterar o parametro da função
agora no else eu nao vou mais gerar um form vazio e sim uma instace=pessoa
tanto no primeiro if quanto no segundo.
lembrando que é preciso recuperar os dados de pessoa = Pessoa.objects.get(request.post, instance= pessoa)


Delete
-a url vai precisar de um id como parametro

na view na funçao remove passe como paramentro o id 
nao precisa armazer em uma variavel o objeto pessoa 
so colocar o delete

Atividade completar o crud com todos os operações:

vamos pular para o 6 da documentação mas antes vamos rever a parte 2 com relacionamento entre moldes


__RETORNO DAS AULAS - POS GREVE__

                ::URL::
a url's possui dois niveis onde temos as urls do app e as urls do projeto

                ::VIEW::

toda view vai receber uma requisição e enviar uma resposta
-como receber uma requisição / request
-como enviar uma resposta / response

Model Form 
-no arquivo html podemos colocar {{form.as_p}} serve para melhorar apresentação

                ::DEPOIS DA REVISÃO::
__Estilização__
CSS
frameWork para estilização: bootsrap
quando vamos trabalhar com templates utilizamos a mecanica de STAtic FILES
onde ficará nosso arquivos que não vao mudar ou seja arquivos estaticos, na documentação part 6 tem falando sobre isso
tutorial 5 "writing your first Django app, part 6"

não utilizar aspas dupas em um caminha que ja esta usando:
ex: href=" use aspas simpes agora { static ...}'"
ctrl +h para pesquisar e fazer modificações no arquivo mais rapido
-href
-img
-svg
-css
{% load static %}
{% block content%} {% endblock %} use em momentos para que o conteudo vai mudar
{% include '_sidebar.html' %} use em situações que não vao mudar e para dar manutenção. lembre-se que é so para incluir
{% extends '_base.html' %}

seguimentar a pagina para melhorar manutenção

os widgests - auxilia a alterar os atributos da minha classe
lembre-se de importa-lo: From django forms or contrib

para quinta feira estilizar tudo no projeto ate agora

eADEFFE