### Exercício 1
#Desenvolva um programa para ler três valores
#numéricos inteiros (`x`, `y` e `z`), que serão
#informados pelo usuário. Destes valores recebidos,
#identificar o maior, o menor e o intermediário, apresentando-os em tela.

x = int(input("Digite o valor de x "))
y = int(input("Digite o valor de y "))
z = int(input("Digite o valor de z "))

if x >= y and x >= z:
    maior = x
    if y >= z:
        intermediario = y
        menor = z
    else:
        intermediario = z
        menor = y
elif y >= x and y >= z:
    maior = y
    if x >= z:
        intermediario = x
        menor = z
    else:
        intermediario = z
        menor = x
else:
    maior = z
    if x >= y:
        intermediario = x
        menor = y
    else:
        intermediario = y
        menor = x


print(f"Maior {maior}")
print(f"Intermediario {intermediario}")
print(f"Menor {menor}")