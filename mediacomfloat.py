#FUAQ Receba duas notas e se a média das das
#duas for maior que 7 escreva "aprovado", senão escreva "exame"

nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))

media = (nota_um + nota_dois) / 2

if media >= 7:
    print("aprovado")
else:
    print("exame")