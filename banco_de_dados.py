import sqlite3

############################################################################
## class BancoDeDados:
##
## Essa classe é responsável por conectar com o banco de dados e fazer a 
## leitura e escrita dos dados
############################################################################


class BancodeDados:

    ########################################################################
    ## No inicializador da classe, verificamos se a tabela de anúncios 
    ## existe, caso ela não exista nós criamos a tabela no arquivo
    ## "database.db"
    ########################################################################
    def __init__(self):
        connection = sqlite3.connect('./database.db')
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS anuncio (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome VARCHAR(50) NOT NULL,
                    cliente VARCHAR(50) NOT NULL,
                    datainicio DATE NOT NULL,
                    datatermino DATE NOT NULL,
                    investimentodia FLOAT NOT NULL
                )""")
        connection.commit()

    ########################################################################
    ## O método "add" é o método da classe responsável por adicionar um
    ## novo anúncio. Ele recebe os parâmetros "nome", "cliente",
    ## "datainicio", "datatermino" e "investimentodia" e os passa para o
    ## o método "execute" que roda a query para inserir os dados no banco de
    ## dados.
    ########################################################################
    def add(self, nome, cliente, datainicio, datatermino, investimentodia):
        connection = sqlite3.connect('./database.db')
        cursor = connection.cursor()

        cursor.execute('INSERT INTO anuncio(nome, cliente, datainicio, datatermino, investimentodia) VALUES(?, ?, ?, ?, ?)',
                       (nome, cliente, datainicio, datatermino, investimentodia))
        connection.commit()

    ########################################################################
    ## O método "getrows" é o método responsável por fazer a leitura dos
    ## dados salvos no banco de dados. Ele recebe os filtros "nome",
    ## "datainicio" e "datatermino". Caso esses filtros sejam passados para
    ## a função, eles são adicionados na query de leitura.
    ########################################################################
    def getrows(self, nome='', datainicio='', datatermino=''):
        filter = ""
        datastring = ""

        if nome:
            filter += 'WHERE nome LIKE "{}"'.format(nome)

        if datainicio and datatermino:
            datastring += 'date(datainicio) >= date("{}") AND date(datatermino) >= date("{}")'.format(datainicio, datatermino)

            if filter:
                filter += ' AND {}'.format(datastring)
            else:
                filter += ' WHERE {}'.format(datastring)

        query = 'SELECT nome, cliente, datainicio, datatermino, investimentodia FROM anuncio {}'.format(filter)
        connection = sqlite3.connect('./database.db')
        cursor = connection.cursor()
        rows = cursor.execute(query).fetchall()

        return rows