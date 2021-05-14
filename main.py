from calculadora_v2 import calculadora
from banco_de_dados import BancodeDados
from utils import parsedata

bd = BancodeDados()


def iniciar():

    print("Você deseja cadastrar um novo anuncio ou imprimir relatorio ?")
    print("Para cadastrar novo anuncio digite: 1")
    print("Para imprimir relatorio digite: 2")
    return int(input("Para fechar o programa digite: 0 \n"))


x = iniciar()

while x != 0:
    if x == 1:
        nome = input("Qual o nome do anuncio ?")
        cliente = input("Qual o cliente ?")
        datainicio = parsedata(input("Qual a data de inicio (Digite no formato dia/mes/ano)? "), '-')
        datatermino = parsedata(input("Qual a data de termino (Digite no formato dia/mes/ano)? "), '-')
        valor = float(input("Qual o valor de investimento diario ? "))
        bd.add(nome, cliente, datainicio, datatermino, valor)
        print("")

    if x == 2:
        data = ""
        data1 = ""
        nome = ""

        print("Para relatorio completo digite: 1 ")
        print("Para relatorio com filtro por nome digite: 2 ")
        print("Para relatorio com filtro por data digite: 3 ")
        y = int(input("Para relatorio com filtro por nome e data digite: 4 \n"))

        if y == 2 or y == 4:
            nome = input("Digite o nome no anuncio que deseja: ")

        if y == 3 or y == 4:
            data = parsedata(input("Digite a data inicial que deseja: "), '-')
            data1 = parsedata(input("Digite a data final que deseja: "), '-')

        results = bd.getrows(nome, data, data1)
        for row in results:
            valores = calculadora(row[4])
            print('O anuncio {} do cliente {} de data de inicio {} e data de termino {}'.format(row[0], row[1], parsedata(row[2], "/", 1), parsedata(row[3], "/", 1)))
            print('Dos R$ {:.2f} investidos, será gerado um total de {:.0f} visualizações dos anúncios.'.format(row[4],valores['visualizacoes']))
            print('Foram gerados {:.0f} cliques e {:.0f} compartilhamentos \n'.format(valores['cliques'], valores['compartilhamentos']))
    if x != 0:
        x = iniciar()




