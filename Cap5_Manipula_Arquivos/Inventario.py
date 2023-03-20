from Funcoes.Funcoes_Arquivos import *

inventario = {}
opcao = chamarMenu()
while opcao > 0 and opcao < 5:
    if opcao == 1:
        registrar(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 4:
        concatenar(inventario)
    elif opcao == 3:
        resultado = exibir()
        for linha in resultado:
            lista = linha.split(";")
            print("Data..........", lista[1])
            print("Descrição.....", lista[2])
            print("Departamento..", lista[3])
            #           print(linha[2:-1]) dessa forma corta o 3 caracter da string ate o ultimo (tirando o numero patrimonial)
            #           print(linha[linha.find(";")+1:-1])  # exibira o prox caractere depois do ";" ate o ultimo
            #  Separando por cada item da lista
            #           separacao = linha[linha.find(";")+1:-1]
            #           data = separacao[0:separacao.find(";")]
            #           separacao = separacao[separacao.find(";")+1:-1]
            #           descricao = separacao[0:separacao.find(";")]
            #           departamento = linha[linha.rfind(";")+1:-1]
            #           print("Data..........",data)
            #           print("Descrição.....",descricao)
            #           print("Departamento..",departamento)
    opcao = chamarMenu()
