def chamarMenu():
    escolha = int(input("Digite\n" 
                  "<1> - Registrar ativo\n"
                  "<2> - Persistir em arquivo\n"
                  "<4> - Concatenar arquivo\n"
                  "<3> - Exibir ativos armazenados\n"))
    return escolha

def registrar(dicionario):
    resp = "S"
    while resp == "S":
        chave = input("Digite o número patrimonial: ")
        dicionario[chave] = [input("Digite a data da última atualização: "),
        input("Digite a descrição: "),
        input("Digite o departamento: ")]
        resp = input("Digite S para continuar: ").upper()

def persistir(dicionario):
    # se usar o met "a" vai acrescentar um "\n" na primeira linha para concatenar (nao vai dar pra usar o met split na imprerssao pq na primeira linha nao vai ter nada)
    with open("inventario.csv", "w") as inv:
        for chave, valor in dicionario.items():
            inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + "\n")
            print("Persistido com sucesso")
    return "Persistido com sucesso"

def concatenar(dicionario):
    with open("inventario.csv", "a") as inv:
        for chave, valor in dicionario.items():
            inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + "\n")
            print("Persistido com sucesso")
    return "Persistido com sucesso"

def exibir():
    with open("inventario.csv", "r") as inv:
        linhas = inv.readlines()
    return linhas

