inventario = []
resposta = 'S'

#Entrada de dados (cadastrando equipamento)
while resposta == 'S':
    equipamento = [input("Equipamento: "),
                   float(input("Valor: ")),
                   int(input("Numero Serial: ")),
                   input("Departamento: ")]
    inventario.append(equipamento)
    resposta = input("Digite S para continuar: ").upper()

# Saida de dados (imprimindo lista)
for elemento in inventario:
    print("Nome.........: ",elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

# Buscando equipamento
busca = input(" Digite o nome do equipamento que desja buscar: ")
for elemento in inventario:
    if busca == elemento[0]:
        print("Valor....: ", elemento[1])
        print("Serial...: ", elemento[2])

# Depreciando um equipamento
depreciacao = input("Digite o nome do equipamento que será depreciado: ")
for elemento in inventario:
    if depreciacao == elemento[0]:
        print("Valor antigo: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Novo valor: ", elemento[1])

# Excluindo um equipamento
serial = int(input("Digite o serial do equipamento que será excluido: "))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)

# imprimindo lista
for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

#resumo de valores do inventario
valores=[]
for elemento in inventario:
  valores.append(elemento[1])
if len(valores)>0:
  print("O equipamento mais caro custa: ", max(valores))
  print("O equipamento mais barato custa: ", min(valores))
  print("O total de equipamentos é de: ", sum(valores))
