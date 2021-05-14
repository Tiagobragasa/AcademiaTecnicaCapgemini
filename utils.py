############################################################################
## function parsedata:
##
## Essa função é utilizada para retornar a data formatada. Ela recebe os
## parâmetros "data", "separator" e "isdb".
############################################################################
def parsedata(data, separator='/', isdb=0):
    ########################################################################
    ## Se a data informada vier do banco de dados faz o split da string
    ## procurando pelo caracter "-", caso não seja, faz o split procurando
    ## por "/".
    ########################################################################
    dataarray = data.split("-" if isdb else "/")
    dataarray.reverse()
    return "{}".format(separator).join(dataarray)