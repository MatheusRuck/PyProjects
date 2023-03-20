nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))
prioritario = "Não"

if idade > 65:
    prioritario = "Sim"

print("O paciente " + nome + " de ", idade, "anos possui atendimento prioritario? " + prioritario )