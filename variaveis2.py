nome=input("Digite um funcionario: ")
empresa=input("Digite a instituição: ")
qtdFuncionario=int(input("Digite a qtd de funcionários: "))
mediaMensalidade=float(input("Digite a média da mensalidade: "))
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtdFuncionario, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))

print("==============Verifique os tipos de dados abaixo:==============")
print("O tipo de dado da variavel [nome] é: ",type(nome))
print("O tipo de dado da variavel [empresa] é: ",type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: ",type(qtdFuncionario))
print("O tipo de dado da variavel [mediaMensalidade] é: ",type(mediaMensalidade))