#FUAQ leia uma temperatura em graus Celsius e
#mostrea convertida em graus Fahrenheit.
#A fórmula de conversão é:  F=(9*C+160) / 5,
#sendo F a temperatura em Fahrenheit e C a
#temperatura em Celsius.

temperatura_celcius = float(input("Temperatura"))

conversao = (9 * temperatura_celcius + 160) / 5

print(f"Celcius {temperatura_celcius}, Fahrenheit {conversao}")