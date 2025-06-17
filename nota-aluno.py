# Crie um programa que receba 5 notas e faça a média delas
# Peça o nome do aluno
# Mostre o nome do aluno e a média

def media(nota_um, nota_dois):
   resultado = (int(nota_um) + int(nota_dois)) / 2
   print(f"A média do aluno foi {resultado}")

primeira_nota = input("Digite a primeira nota ")
segunda_nota = input("Digite a segunda nota ")

media(primeira_nota, segunda_nota)

def media(lista_notas):
   resultado = (sum(lista_notas)) / 5
   nome = input("Digite o nome do aluno ")
   return resultado, nome

lista = []
for i in range(0, 5):
   nota = float(input(f"Digite a nota {i+1} "))
   lista.append(nota)

media_do_aluno, nome = media(lista)
print(f"O vivente {nome} teve média= {media_do_aluno}")

lista_notas = []
def media(notas):
   soma = sum(notas)
   quantidade = len(notas)
   resultado = soma / quantidade
   return resultado

while(True):
   valor = input("Digite uma nota, ou sair para terminar")
   if valor == "sair":
     break
   lista_notas.append(float(valor))

resultado = media(lista_notas)
print(resultado)
