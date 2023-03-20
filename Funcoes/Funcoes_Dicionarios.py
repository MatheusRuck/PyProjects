def perguntar():
    resposta = input("O que deseja fazer? \n"
                     + "<I> - Para Inserir um usúario \n"
                     + "<P> - Para Pesquisar um usúario \n"
                     + "<E> - Para Excluir um usúario \n"
                     + "<L> - Para Listar um usúario \n").upper()
    return resposta

def inserir(dicionario):
    chave = input("Digite o login: ").upper()
    dicionario[chave] = [input("Digite o nome: ").upper(),
                       input("Digite a última data de acesso: "),
                       input("Qual a última estação acessada: ").upper()]

def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])

def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Objeto Eliminado")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto.......")
        print("Login: ", chave)
        print("Dados: ", valor)
