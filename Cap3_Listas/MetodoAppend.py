inventario=[]
resposta= "S"
while resposta =="S":
    inventario.append(input("Equipamentos: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número Serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite S para continuar: ").upper()


#foreach -> percorre toda lista
for elemento in inventario:
    print("--> ", elemento)