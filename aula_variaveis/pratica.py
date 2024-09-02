var1: str = "Elton Rodrigues"
var2: str = "José Paulo R."
var3: str = "M. Eduarda Alves"

quant = len(var1) + len(var2) + len(var3)

print("Quantidade de letras:", quant)

paragrafo1="abcdefghijklmnopqrstuvwxyz"
paragrafo2= "aeiou" 

alfaInverso = sorted(paragrafo1, reverse=True)
vogaisInverso = sorted(paragrafo2, reverse=True)
print(alfaInverso)
print(vogaisInverso)
