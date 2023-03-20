from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="wazeyes")

opcao = int(input("1 - pesquisar por endereco \n2 - pesquisar por coordenadas \n"))
if opcao == 1:
    endereco=input("Digite um endereco com número e cidade. \n"
                   "Exemplo: avenida paulista, 100 São Paulo: \n")
    resultado = str(geolocator.geocode(endereco)).split(",")
    location = geolocator.geocode(endereco)

    if resultado[0]!='None':
        print("Endereço completo.: ", resultado)
        print("Bairro............: ", resultado[1])
        print("Cidade............: ", resultado[2])
        print("Regiao............: ", resultado[3])
        print("Coordenadas.......: ", location.latitude, location.longitude)

elif opcao == 2:
    latitude=float(input("Digite a latitude...: "))
    longitude=float(input("Digite a longitude.: "))

    resultado = str(geolocator.reverse(f"{latitude}, {longitude}")).split(",")
    if resultado[0]!='None':
        print("Endereço completo.: ", resultado)
        print("Dado 1............: ", resultado[0])
        print("Dado 2............: ", resultado[1])
        print("Dado 3............: ", resultado[2])
