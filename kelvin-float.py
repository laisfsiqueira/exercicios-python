#FUAQ (Faça um algoritmo que) leia um valor de
#temperatura em graus Celsius,
#calcule e exiba a temperatura correspondente em graus Kelvin
#(sabendo que Kelvin = Celsius + 273).

valor = float(input("Digite uma temperatura em Celcius "))

valor_convertido = valor + 273

print(f"Celcius: {valor} Kelvin: {valor_convertido}")