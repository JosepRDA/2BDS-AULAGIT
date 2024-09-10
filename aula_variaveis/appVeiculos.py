numeroDeRodas = int(input("Digite a quantidade de rodas do seu veículo: "))

match numeroDeRodas:
    case 2:
        print("Seu veículo é uma Moto")
    case 4:
        print("Seu veículo é um carro")
    case 6:
        print("Seu veículo é um caminhão pequeno")
    case 8 | 10 | 12:
        print("Seu veículo é um caminhão grande")
    case _:
        print("Veículo desconhcido.")

print()
print("=====FIM DO PROGRAMA=====")