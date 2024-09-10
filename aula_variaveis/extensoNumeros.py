# de um até nove

while True:
    numero: int = 0
    try:
        numero = int(input("Digite um numero de 1 a 9: "))
    except ValueError:
        print("Digite um número.")
    try: 
        match numero:
            case 1:
                print("UM")
                break
            case 2:
                print("DOIS")
                break
            case 3:
                print("TRES")
                break
            case 4:
                print("QUATRO")
                break
            case 5:
                print("CINCO")
                break
            case 6:
                print("SEIS")
                break
            case 7:
                print("SETE")
                break
            case 8:
                print("OITO")
                break
            case 9:
                print("NOVE")
                break
            case _:
                print("Digite entre 1-9.")
    except NameError:
        print("você não digitou um número.")