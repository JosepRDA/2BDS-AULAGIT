numero = int(input("Digite um numero: "))

if (numero % 4 == 0 and numero % 100 != 0) or (numero % 400 == 0):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")
