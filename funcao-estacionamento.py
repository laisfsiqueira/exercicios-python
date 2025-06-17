def calculo(nome, quantidade_horas):
  valor = 0
  if quantidade_horas <= 2:
    valor = 5
  else:
    valor = (quantidade_horas - 2) * 3 + 5

  print(f"O usuário {nome} deve pagar {valor}R$")

while(True):
  print("Digite o nome do usuário ou sair")
  nome = input()
  if nome == "sair":
    break
  else:
    print(f"Digite a quantidade de horas que {nome} permaneceu no estacionamento")
    quantidade = int(input())
    calculo(nome, quantidade)

