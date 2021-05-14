import sqlite3


class BancodeDados:

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

    def add(self, nome, cliente, datainicio, datatermino, investimentodia):
        connection = sqlite3.connect('./database.db')
        cursor = connection.cursor()

        cursor.execute('INSERT INTO anuncio(nome, cliente, datainicio, datatermino, investimentodia) VALUES(?, ?, ?, ?, ?)',
                       (nome, cliente, datainicio, datatermino, investimentodia))
        connection.commit()

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