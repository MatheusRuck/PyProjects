equipamentos = []
valor = []
numeroSerial = []
depart = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Digite o equipamento: "))
    valor.append(float(input("Digite o valor: ")))
    numeroSerial.append(int(input("Digite o número serial: ")))
    depart.append(input("Digite o departamento: "))

    resposta = input("Digite S para continuar: ").upper()

for indice in range (0,len(equipamentos)):
    print( "\nEquipamento...: ", (indice+1))
    print("Nome..........: ", equipamentos[indice])
    print("Valor.........: ", valor[indice])
    print("Serial........: ", numeroSerial[indice])
    print("Departamento..: ", depart[indice])


fazerBusca = 0
while fazerBusca != 4:
    fazerBusca = int(input("\n 1)Fazer uma busca \n 2)Depreciar um valor \n 3)Eliminar um equipamento   \n 4)Sair \n"))
    # FAZENDO UMA BUSCA NA LISTA
    if fazerBusca == 1:
        busca = input("\nDigite o nome do equipamento que deseja buscar: ")
        for indice in range (0,len(equipamentos)):
            if busca == equipamentos[indice]:
                print("Valor...: ", valor[indice])
                print("Serial..: ", numeroSerial[indice])

    #FAZENDO UMA DEPRECIAÇÃO NO VALOR
    elif fazerBusca == 2:
        deprec = input("\n Digite o nome do equipamento que será depreciado: ")
        deprecValor = float(input("\n Digite a porcentagem que será depreciado: "))/100
        for indice in range (0, len(equipamentos)):
            if deprec == equipamentos[indice]:
                print("\n Valor...: ", valor[indice])
                print("\n Valor que sera descontado..: ", deprecValor*valor[indice])
                valor[indice] = valor[indice] * (1-deprecValor)
                print("\n Valor final...: ",valor[indice])

    #ELIMINANDO UM EQUIPAMENTO
    elif fazerBusca == 3:
        delete = int(input("\n Digite o número serial que deseja excluir: "))
        for indice in range (0, len(equipamentos)):
            if delete == numeroSerial[indice]:
                del depart[indice]
                del valor[indice]
                del equipamentos[indice]
                del numeroSerial[indice]
                break


for indice in range (0,len(equipamentos)):
    print( "\n \nEquipamento...: ", (indice+1))
    print("Nome..........: ", equipamentos[indice])
    print("Valor.........: ", valor[indice])
    print("Serial........: ", numeroSerial[indice])
    print("Departamento..: ", depart[indice])




