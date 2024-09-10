nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7 and media < 11:
    print("O aluno está na média.")
else:
    print("O aluno não está na média.")