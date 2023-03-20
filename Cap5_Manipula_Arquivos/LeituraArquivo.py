# "r" -> ler o arquivo
with open("teste.txt" , "r") as arquivo:
    conteudo = arquivo.read()   #metodo read vem como string, readlines quebra as linhas em lista
print("Tipo de variavel: ", type(conteudo))
print("Conteudo do arquivo: ", conteudo)