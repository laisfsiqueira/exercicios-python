# Programa para identificar o animal com base em 3 classificações

# Leitura das 3 palavras de entrada
valor1 = input().strip()  # vertebrado ou invertebrado
valor2 = input().strip()  # ave, mamifero, inseto ou anelideo
valor3 = input().strip()  # carnivoro, onivoro, herbivoro ou hematofago

# Verifica se é vertebrado
if valor1 == "vertebrado":
    if valor2 == "ave":
        if valor3 == "carnivoro":
            print("aguia")
        else:  # onivoro
            print("pomba")
    else:  # mamifero
        if valor3 == "onivoro":
            print("homem")
        else:  # herbivoro
            print("vaca")

# Verifica se é invertebrado
else:  # invertebrado
    if valor2 == "inseto":
        if valor3 == "hematofago":
            print("pulga")
        else:  # herbivoro
            print("lagarta")
    else:  # anelideo
        if valor3 == "hematofago":
            print("sanguessuga")
        else:  # onivoro
            print("minhoca")