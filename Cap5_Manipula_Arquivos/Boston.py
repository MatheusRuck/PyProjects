with open("economic-indicators.csv", "r") as boston:
    total_voos = 0
    maior = 0
    total_passageiros = 0
    maior_media_diaria = 0
    total_jobs = 0.0
    ano_usuario = input("Qual ano deseja pesquisar: ")

    for linha in boston.readlines()[1:-1]:
        lista = linha.split(",")
        total_voos = total_voos + float(lista[3]) #pegando o 4 valor separando por virgula
        #analisando o ano e mes q teve maior qtd de passageiros
        if float(lista[2]) > float(maior):
            maior = lista[2]
            ano = lista[0]
            mes = lista[1]
        #qtd de desemprego no ano pesquisado
        if ano_usuario == lista[0]:
            total_jobs = total_jobs + float(lista[7])
        #qtd de passageiros no ano pesquisado
        if ano_usuario == lista[0]:
            total_passageiros = total_passageiros + float(lista[2])
            #pegando a maior media diaria e o mes da maior media diaria
            if float(lista[5]) > float(maior_media_diaria):
                maior_media_diaria = lista[5]
                mes_maior_diaria = lista[1]

    print("O total do voos é ",total_voos)
    print("O mes/ano de maior movimento no aeroporto foi: ", str(mes), "/",str(ano))
    print("O total de passageiros do ano ", ano_usuario, "foi de ",total_passageiros)
    print("O mes do ano ", ano_usuario," com maior media diaria de hotel foi ", mes_maior_diaria)
    print("Porcentagem de desemprego no ano pesquisado: ", total_jobs*100 , "%")