
valor = int(input("Digite o valor de n: "))

aux = 1

while (valor > 1):
    aux *= valor
    valor -= 1

print(aux)
