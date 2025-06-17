# -*- coding: utf-8 -*-

valor1 = float(input())
valor2 = float(input())
valor3 = float(input())
valor4 = float(input())
valor5 = float(input())
valor6 = float(input())
positivos = []
if valor1 > 0:
    positivos = [valor1]
if valor2 > 0:
    positivos.append(valor2)
if valor3 > 0:
    positivos.append(valor3)
if valor4 > 0:
    positivos.append(valor4)
if valor5 > 0:
    positivos.append(valor5)
if valor6 > 0:
    positivos.append(valor6)
leng = len(positivos)
print(f"{leng} valores positivos")