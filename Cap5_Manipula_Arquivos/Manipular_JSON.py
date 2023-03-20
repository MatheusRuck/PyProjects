from Funcoes.Funcoes_JSON import *

inventario = lerArquivo("inventario_json.json")
opcao=chamarMenu()
while opcao>0 and opcao<4:
    if opcao==1:
        print(registrar(inventario, "inventario_json.json"))
    elif opcao==2:
        exibir("inventario_json.json")
    elif opcao == 3:
        excluir(inventario, "inventario_json.json")
    opcao = chamarMenu()