#calcular fatorial


print("=====FATORIAL=====")

numbero = int(input("Digite um numero: "))
fatorial = 1

for i in range(1, numbero + 1):
    fatorial = fatorial * i

print(f"o fatorial de {numbero} é {fatorial}")