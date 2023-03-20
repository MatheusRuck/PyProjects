from Cap3_funcoes.IdentificacaoDeFuncoes import *

minhaLista = []
print("Preenchendo")
preencherInventario(minhaLista)
print("\nExibindo")
exibirInventario(minhaLista)

print("\nPesquisando")
localizarPorNome(minhaLista)
print("\nAlterando")
depreciarPorNome(minhaLista, int(input("informe valor da depreciacao: ")))

print("\nExcluindo")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("\nResumindo")
resumirValores(minhaLista)