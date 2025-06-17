# dicionario = {
#   'livro': 'Sherlock Holmes',
#   'author': 'Sir Arthur Connan Doyle',
#   'ano': 1902
# }

#dicionario.update({"ano": 1902})

# for chave in dicionario.keys():
#   print(chave)

# for valor in dicionario.values():
#   print(valor)

# for chave, valor in dicionario.items():
#   print(f"{chave}: {valor}")

biblioteca = []
sequencia = 0

def menu():
  print("1 - Inserir novo Livro")
  print("2 - Procurar livro por id")
  print("3 - Procurar livro por titulo")
  print("4 - Obter preço total dos livros")
  print("5 - Listar todos os livros")
  print("0 - Sair")

def inserir_livro(sequencia):
  titulo = input("Digite o titulo do livro: ")
  autor = input("Digite o autor do livro: ")
  ano = input("Digite o ano do livro: ")
  genero = input("Digite o genero do livro: ")
  preco = float(input("Digite o preço do livro: "))

  livro = {
    "titulo": titulo,
    "autor": autor,
    "ano": ano,
    "genero": genero,
    "id": sequencia,
    "preco": preco
  }
  biblioteca.append(livro)

def listar():
  for livro in biblioteca:
    print("")
    for chave, valor in livro.items():
      if chave == "preco":
        print(f"{chave}: R$ {valor}")
      else:
        print(f"{chave}: {valor}")
    print("")

def total():
  total = 0
  for livro in biblioteca:
    total = total + livro["preco"]
  print(f"O valor total do carrinho de compras é R$ {total}")

while(True):
  menu()
  opcao = int(input("Escolha uma das opções acima: "))
  match opcao:
    case 0:
      break
    case 1:
      sequencia += 1
      inserir_livro(sequencia)
    case 4:
      total()
    case 5:
      listar()
    case _:
      print("Digite uma opção válida")