import sqlite3 as sq

carros = {}

class database:

    def __init__(self):
        self.con = sq.connect("Database.db")
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS carros(MARCA, COR)")
        self.con.commit()

    def cadastrarCarro(self, Nome, Cor):
        self.cur.execute(f"INSERT INTO carros(MARCA, COR) VALUES ('{Nome.lower()}', '{Cor.lower()}')")
        self.con.commit()

    def updateCarro(self, Nome, Cor):
        self.cur.execute(f"UPDATE carros SET COR='{Cor}' WHERE MARCA='{Nome.lower()}'")
        self.con.commit()

    def listCarros(self):

        data = self.cur.execute(f"SELECT * FROM carros")


        return self.cur.fetchall()
    
    def excluirCarro(self, Nome):
        self.cur.execute(f"DELETE FROM carros WHERE MARCA='{Nome.lower()}'")
        self.con.commit()

d = database()

def setupCarros():
    carros.clear()
    for i in d.listCarros():
        carros[i[0]] = i[1]


def visualizar():

    print("\n\nCarros encontrados: ")

    for i in carros:
        print(i + " -> " + carros[i])

    print("\n\n")

def exists(name):
    
    return carros.get(name.lower()) != None

def cadastro():
    name = input("Digite o nome do carro: ")
    cor = input("Digite a cor do carro: ")

    d.cadastrarCarro(name, cor)

    print("\n\n\n\n\nCarro cadastrado com sucesso!! \n\n")

def editar():
    name = input("Digite o nome do carro: ")

    if exists(name):

        cor = input("Digite a nova cor: ")

        d.updateCarro(name, cor)

        print("\n\nCarro atualizado com sucesso!! \n\n")

    else:
        print("\nCarro não encontrado em nosso banco de dados. \n")

def excluir():

    name = input("Digite o nome do carro: ")

    if exists(name):
        try:
            d.excluirCarro(name)
        except :

            print(f"\n\n\n\n\n Houve um erro ao tentar excluir o carro: {name}")

        else:
            print("\n\n\n\n\nCarro deletado com sucesso!! \n\n")
    else: 
        print("\nCarro não encontrado em nosso banco de dados. \n")
        
while True:

    setupCarros()

    print("BRASIL CARROS: \n")
    print("""
    1- cadastrar
    2- visualizar
    3- editar
    4 excluir
    """)
    op = int(input("escolha uma opçao: "))
    if op == 1:
        cadastro()
    elif op == 2:
        visualizar()
    elif op == 3:
        editar()
    elif op == 4:
        excluir()
    else:
        print("opçao invalida")    