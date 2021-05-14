valor = float(input('Quantos reais você quer investir em anúncios?: R$ '))

click = ((valor * 30) * 12)/100
compartilhamentos = (click * 3)/20
novas_visualizacoes = compartilhamentos * 40
visualizacoes = novas_visualizacoes
visualizacoes_iniciais = (valor * 30)

for i in range(3):
    click = (visualizacoes * 12) / 100
    compartilhamentos = (click * 3) / 20
    visualizacoes = compartilhamentos * 40
    visualizacoes_iniciais += visualizacoes

visualizacoes_totais = visualizacoes_iniciais + novas_visualizacoes
print('Dos R$ {:.2f} investidos, será gerado um total de {:.0f} visualizações dos anúncios.'.format(valor, visualizacoes_totais))