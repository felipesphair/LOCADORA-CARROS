carros = []
def cadastro():
    
    name = input("Digite o nome do carro: ")
    cor = input("Digite a cor do carro: ")
    carro = {
    'carro': name,
    'cor': cor
    }
    carros.append(carro)
    return carro
    
def visualizar():
    busca = input("qual carro deseja buscar: ")
    for carro in carros:
        if carro["carro"] == busca:
            print(carro) 

def exists(busca):

    e = False

    for i in carros:
        if i["carro"] == busca:
            e = True

    return e 

def editar():
    editar = input("qual carro deseja editar: ")
    i = 0
    if exists(editar):
        for carro in carros:
            if carro["carro"] == editar:
                replace = input("editar a cor por: ")
                carros[i] = {"carro": editar, "cor": replace}
                print('ediçao realizada com sucesso')
            i += 1
    else:
        print("carro nao encontrado")
        cad = input("deseja cadastrar? s/n: ")
        if cad == "s":
            cadastro()
        else:
            return None


        
def excluir():
    excluir = input("qual carro deseja excluir: ")
    i = 0 
    for carro in carros:
        if carro["carro"] == excluir.lower():
            carros.pop(i)       
            print('exclusao realizada com sucesso')

        i += 1 
def ops():
    while True:
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


ops()