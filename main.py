############################################################################
## Aqui importamos as funções e classes que serão utilizadas.
############################################################################
from calculadora import calculadora
from banco_de_dados import BancodeDados
from utils import parsedata

############################################################################
## Aqui iniciamos a classe que é responsável pela leitura e escrita dos
## dados.
############################################################################
bd = BancodeDados()


############################################################################
## function iniciar:
##
## Essa função é responsável por exibir as opções do menu principal e
## retorna a opção inserida pelo usuário.
############################################################################
def iniciar():

    print("Você deseja cadastrar um novo anuncio ou imprimir relatorio ?")
    print("Para cadastrar novo anuncio digite: 1")
    print("Para imprimir relatorio digite: 2")
    return int(input("Para fechar o programa digite: 0 \n"))

############################################################################
## Aqui nós iniciamos a variável x para iniciar o loop que ficará
## rodando enquanto o usuário escolher uma das opções que não seja sair
## do programa.
############################################################################
x = iniciar()

## Enquanto x for diferente de 0 executa o programa
while x != 0:
    ########################################################################
    ## Se x for igual a 1, o usuário insere o nome do anúncio, cliente, data
    ## de início do anúncio, data de término do anúncio e valor investido.
    ## Após receber esses valores chama a função add da classe BancoDeDados
    ## passando esses valores para serem salvos no banco de dados.
    ########################################################################
    if x == 1:
        nome = input("Qual o nome do anuncio ?")
        cliente = input("Qual o cliente ?")
        datainicio = parsedata(input("Qual a data de inicio (Digite no formato dia/mes/ano)? "), '-')
        datatermino = parsedata(input("Qual a data de termino (Digite no formato dia/mes/ano)? "), '-')
        valor = float(input("Qual o valor de investimento diario ? "))
        bd.add(nome, cliente, datainicio, datatermino, valor)
        print("") ## <----- pode apagar esse print e comitar

    ########################################################################
    ## Se a x for igual a 2, o usuário escolherá o tipo de relatório, que
    ## pode ser, completo, com filtro por nome, filtro por data ou filtro
    ## por data e nome.
    ########################################################################
    if x == 2:
        data = ""
        data1 = ""
        nome = ""

        print("Para relatorio completo digite: 1 ")
        print("Para relatorio com filtro por nome digite: 2 ")
        print("Para relatorio com filtro por data digite: 3 ")
        y = int(input("Para relatorio com filtro por nome e data digite: 4 \n"))

        #####################################################################
        ## Se y for igual a 2 (relatório completo) ou 4 (relatório por nome
        ## e data), o usuário insere o nome.
        #####################################################################
        if y == 2 or y == 4:
            nome = input("Digite o nome no anuncio que deseja: ")

        #####################################################################
        ## Se y for igual a 3 (relatório por data) ou 4 (relatório por nome
        ## e data), o usuário insere a data inicial e a data final.
        #####################################################################
        if y == 3 or y == 4:
            data = parsedata(input("Digite a data inicial que deseja: "), '-')
            data1 = parsedata(input("Digite a data final que deseja: "), '-')

        #####################################################################
        ## Após popular os dados do filtro chama a função getrows da classe
        ## BandoDeDados para fazer a leitura dos dados.
        #####################################################################
        results = bd.getrows(nome, data, data1)
        
        #####################################################################
        ## Executa um loop e exibe os resultados retornados.
        #####################################################################
        for row in results:
            valores = calculadora(row[4])
            print('O anuncio {} do cliente {} de data de inicio {} e data de termino {}'.format(row[0], row[1], parsedata(row[2], "/", 1), parsedata(row[3], "/", 1)))
            print('Dos R$ {:.2f} investidos, será gerado um total de {:.0f} visualizações dos anúncios.'.format(row[4],valores['visualizacoes']))
            print('Foram gerados {:.0f} cliques e {:.0f} compartilhamentos \n'.format(valores['cliques'], valores['compartilhamentos']))
    if x != 0:
        x = iniciar()




