def cifra_cesar_array(texto, deslocamento, modo='cifrar'):
    alfabeto = list("abcdefghijklmnopqrstuvwxyz")
    resultado = ''
    tamanho = len(alfabeto)

    for char in texto:
        if char in alfabeto:
            indice = alfabeto.index(char)
            if modo == 'cifrar':
                novo_indice = (indice + deslocamento) % tamanho
            elif modo == 'decifrar':
                novo_indice = (indice - deslocamento) % tamanho
            resultado += alfabeto[novo_indice]
        else:
            resultado += char
    return resultado

mensagem = "Ataque ao Amanhecer"
deslocamento = 3

cifrada = cifra_cesar_array(mensagem, deslocamento, modo='cifrar')
#decifrada = cifra_cesar_array(cifrada, deslocamento, modo='decifrar')

print("Original :", mensagem)
print("Cifrada  :", cifrada)
#print("Decifrada:", decifrada)