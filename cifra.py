def cifrar(mensagem, alfabeto):
  mensagem_lista = list(mensagem)
  alfabeto_lista = list(alfabeto)

  mensagem_cifrada = []

  for letra in mensagem_lista:
    if letra.isalpha():
      indice = alfabeto_lista.index(letra)
      mensagem_cifrada.append(alfabeto[(indice + 3) % 26])
    else:
      mensagem_cifrada.append(letra)

  print("".join(mensagem_cifrada))



alfabeto = "abcdefghijklmnopqrstuvwxyz"
mensagem = "ataque as 21"

cifrar(mensagem, alfabeto)
