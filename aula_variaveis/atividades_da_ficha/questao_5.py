# sequencia de fibonnacci

print("=====SEQUENCIA DE FIBONACCI=====")

numbero = int(input("Digite um numero: "))

a = 0
b = 1

while a <= numbero:
    print(a, end=" ")

    temp = b
    b = a + b
    a = temp