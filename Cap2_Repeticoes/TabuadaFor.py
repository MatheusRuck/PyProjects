
# for numero in range(1,int(input("Digite um numero para determinar o fim: ")),1):
# print ("	" + str(numero))

numero = int(input("Informe o numero: "))
for x in range(1, 11, 1):
    print(" \t ", numero, " x ", x, " = ", numero*x," \n")


tabuada=int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número ", tabuada)
for valor in range(1,11,1):
   print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))