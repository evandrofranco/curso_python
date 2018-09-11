
a = int(input("Digite um número inteiro:"))
b = a
contador = 0

while (b != 0):
    if(a % b == 0):
        contador += 1
    b -= 1

if contador <= 2:
    print("primo")
else:
    print("não primo")
