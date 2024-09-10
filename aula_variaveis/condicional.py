#E = AND
#OU = OR
#NÃO = NOT!
idade = int(input("Digite sua idade: \n"))
escolha = int(input("Digite 1 para habilitado e 2 para não habilitado: \n"))

habilitado = True if escolha == 1 else False

if idade >= 18 and habilitado == True:
    print("Você pode dirigir.")
    print("Idade e habilitação corretas.")
elif habilitado == True and idade < 18:
    print("Você é habilitado mas não têm idade o suficiente.")
elif idade < 18:
    print("Menor de idade não dirige, mesmo com habilitação.")
elif habilitado == False:
    print("Você não tem habilitação.")
else:
    print("Você não pode dirigir.")

