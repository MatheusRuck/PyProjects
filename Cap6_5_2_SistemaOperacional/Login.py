import getpass

usuario = input("Digite o usuário: ").upper()
senha = getpass.getpass("Digite a senha: ")

if usuario == "RUCK" and senha == "1995":
    print("Usuário logado")
else:
    print("Login Negado")