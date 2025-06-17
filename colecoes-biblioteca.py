def procurar_id(numero):
    for livro in biblioteca:

 if livro["id"] == numero:
    print("")

 for chave, valor in livro.items():
    if chave == "preco":
    print(f"{chave}: R$ {valor}")

else:
    print(f"{chave}: {valor}")
    print("")