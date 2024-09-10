
while True:
    numero: int = 0
    try:
        numero = int(input("Digite um numero entre 1 a 2: "))
    except ValueError:
        print("Digite um número.")
    try: 
        match numero:
            case 1:
                print("O NUMERO 1 FOI DIGITADO.")
                break
            case 2:
                print("O NUMERO 2 FOI DIGITADO.")
                break
            case _:
                print("Digite entre 1 a 2.")
    except NameError:
        print("você não digitou um número.")