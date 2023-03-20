# "w" -> cria e escreve
with open("teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tão facil criar um arquivo.")

# "a" -> concatena, se nao usar a funcao "a" o arquivo é sobreescrito
with open("teste.txt", "a") as arquivo:
    arquivo.write("\nContinuação do txt")

