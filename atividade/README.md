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