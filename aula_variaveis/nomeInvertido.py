# isso printa o cabeçalho do programa
print("="*25)

# exibe o nome de programa
print(" = INVERTEDOR DE NOMES =")

# finaliza o cabeçalho
print("="*25)

# isso pega o nome do usuário usando a função input
nome = input("Digite seu nome completo: ")

# cria uma string vazia e usa o método join e reversed para transformá-la no reverso do nome
nomeInvertido = "".join(reversed(nome))

# exibe o nome em maiúsculo por meio do método upper()
print("Seu nome é", nome.upper())

# exibe a quantidade de caracteres do nome por meio do método __len__()
print("Seu nome possui", nome.__len__(), "letras")

# exibe o valor da variavel nomeInvertido
print("Seu nome invertido seria", nomeInvertido)