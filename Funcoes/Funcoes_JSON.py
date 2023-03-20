import json
import os

def chamarMenu():
    escolha = int(input("Digite: "
                        "\n <1> Registrar ativo"
                        "\n <2> Exibir ativos"
                        "\n <3> Excluir ativos"))
    return escolha

def lerArquivo(arquivo):
    if os.path.exists(arquivo):
        with open (arquivo, "r") as arq_json:
            dicionario = json.load(arq_json)

    else:
        dicionario = {}

    return dicionario

def gravarArquivo(dicionario,arquivo):
    with open(arquivo, "w") as arq_json:
        json.dump(dicionario, arq_json)

def registrar(dicionario, arquivo):
    resp = "S"
    while resp == "S":
        chave = input("Digite o numero patrimonial: ")
        dicionario[chave] = [
            input("Digite a data da ultima atualização: "),
            input("Digite a descrição: "),
            input("Digite o departamento: ")]

        resp = input("Digite <S> para continuar. ").upper()
        gravarArquivo(dicionario, arquivo)
    return "JSON gerado!!!"

def exibir(arquivo):
    dicionario = lerArquivo(arquivo)
    for chave, dado in dicionario.items():
        print("Data.........: ", dado[0])
        print("Descrição....: ", dado[1])
        print("Departamento.: ", dado[2])

def excluir(dicionario, arquivo):
    resp = input("Digite S se deseja limpar arquivo:  ").upper()
    if resp == "S":
        os.remove(arquivo)
        print("Arquivo eliminado")

    chave = input("Informe a chave que deseja excluir: ")
    print(dicionario[chave])
    del dicionario[chave]
    gravarArquivo(dicionario, arquivo)
    print("\nDicionario excluido")
