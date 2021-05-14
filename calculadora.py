
############################################################################
## function calculadora:
##
## Essa função é responsável por calcular o total de cliques,
## compartilhamentos e visualizações. Ela faz o cálculo e retorna um objeto
## com os valores "cliques" sendo o número total de cliques,
## "compartilhamentos" sendo o máximo de compartilhamentos e "visualizacoes"
## sendo o máximo de visualizações.
############################################################################
def calculadora(valor):

    click = ((valor * 30) * 12)/100
    compartilhamentos = (click * 3)/20
    novas_visualizacoes = compartilhamentos * 40
    visualizacoes = novas_visualizacoes
    visualizacoes_iniciais = (valor * 30)
    click01 = click
    soma_compartilhamentos = compartilhamentos

    for i in range(3):
        click = (visualizacoes * 12) / 100
        compartilhamentos = (click * 3) / 20
        visualizacoes = compartilhamentos * 40
        visualizacoes_iniciais += visualizacoes
        click01 += click
        soma_compartilhamentos += compartilhamentos

    max_cliques = click01 + click
    max_compatilhamentos = soma_compartilhamentos + compartilhamentos
    visualizacoes_totais = visualizacoes_iniciais + novas_visualizacoes

    data = dict()
    data['cliques'] = max_cliques
    data['compartilhamentos'] = max_compatilhamentos
    data['visualizacoes'] = visualizacoes_totais

    return data







