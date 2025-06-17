#FUAQ receba um valor de um produto e que
#escreva o novo valor tendo em vista que o desconto foi de 5%.

valor = float(input("Digite o valor do produto "))

desconto = valor * 0.05

valor_final = valor - desconto

print(f"O preço ficou {valor_final}")
