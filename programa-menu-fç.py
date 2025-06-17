def menu():
  menu = """
1. Calcular média de um aluno
2. Calcular valor do estacionamento
3. Cante uma canção de ninar
9. Sair
  """
  print(menu)

def media(nota_um, nota_dois):
  resultado = (int(nota_um) + int(nota_dois)) / 2
  print(f"A média do aluno foi {resultado}")

def calculo(nome, quantidade_horas):
  valor = 0
  if quantidade_horas <= 2:
    valor = 5
  else:
    valor = (quantidade_horas - 2) * 3 + 5

  print(f"O usuário {nome} deve pagar {valor}R$")

def cancao():
  print("borboletinha ta la na cozinha....")






while(True):
  # print("Escolha uma opção: ")
  menu()
  valor = int(input("Escolha uma opção: "))

  if(valor == 1):
    nota_um = int(input("Digite a primeira nota"))
    nota_dois = int(input("Digite a segunda nota"))
    media(nota_um, nota_dois)
  elif valor == 2:
    nome = input("Digite o nome do vivente")
    qtd = int(input("Quantas horas você ficou estacionado?"))
    calculo(nome, qtd)
  elif valor == 3:
    cancao()
  elif valor == 9:
    break
