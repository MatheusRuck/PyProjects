from pygeocoder import Geocoder
key = "AIzaSyAiEkn0VQE5UWWiACxp4XCSH4R_pImB9ns"
endereco = input("Informe o endereço (Ex: 100, Paulista, Sao paulo, SP): \n")
coordenadas = Geocoder(key).geocode(endereco).coordinates
enderecoCompleto = Geocoder(key).geocode(endereco)
cep = Geocoder(key).geocode(endereco).postal_code
pais = Geocoder(key).geocode(endereco).country
estado = Geocoder(key).geocode(endereco).state

print("ENDEREÇO....: ",enderecoCompleto)
print("PAIS........: ",pais)
print("ESTADO......: ",estado)
print("CEP.........: ",cep)
print("COORDENADAS.: ",coordenadas)
print("\n \n #####BUSCANDO PELAS COORDENADAS#####")
lat = float(input("Latitude: "))
long = float(input("Longitude: "))
print(Geocoder(key).reverse_geocode(lat, long))


