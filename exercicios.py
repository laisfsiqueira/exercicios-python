### Exercício 1

#Desenvolva um programa para ler três valores numéricos inteiros (`x`, `y` e `z`), que serão informados pelo usuário. Destes valores recebidos, identificar o maior, o menor e o intermediário, apresentando-os em tela.

#python
x = int(input("Digite o valor de x "))
y = int(input("Digite o valor de y "))
z = int(input("Digite o valor de z "))

if x >= y and x >= z:
    maior = x
    if y >= z:
        intermediario = y
        menor = z
    else:
        intermediario = z
        menor = y
elif y >= x and y >= z:
    maior = y
    if x >= z:
        intermediario = x
        menor = z
    else:
        intermediario = z
        menor = x
else:
    maior = z
    if x >= y:
        intermediario = x
        menor = y
    else:
        intermediario = y
        menor = x


print(f"Maior {maior}")
print(f"Intermediario {intermediario}")
print(f"Menor {menor}")

### Exercício 2

#Solicite ao usuário um valor inteiro. Avalie a paridade do valor informado, escrevendo em tela **PAR** ou **ÍMPAR**.

#python
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("PAR")
else:
    print("ÍMPAR")


### Exercício 3

#A Universidade de Passo Fundo passará a utilizar um sistema de avaliação baseado em conceitos. Contudo, seus professores estão acostumados a mensurar o aprendizado dos estudantes em uma escala de 0 a 100 pontos. Para tornar o processo de transição mais simples, a Pró-reitoria de Ensino encaminhou uma tabela de conversão de notas para conceitos. Assim, a média ponderada das avaliações semestrais de cada disciplina deverão ser convertidas pelos professores com base nesta tabela de referência. Cabe ressaltar que todo professor é obrigado a realizar `3` avaliações a cada semestre, com pesos `20`, `30` e `50`, respectivamente.


#| Intervalo de notas | Conceito | Resultado |
#| ------------------ | -------- | --------- |
#| 0 - 20             | E        | REPROVADO |
#| 21 - 40            | D        | REPROVADO |
#| 41 - 60            | C        | EXAME     |
#| 61 - 80            | B        | APROVADO  |
#| 81 - 100           | A        | APROVADO  |

#Com base nisso, pede-se que seja criado um programa que leia 3 notas (valores inteiros entre 0 e 100, obrigatoriamente). Com os valores lidos, apresente para o usuário a **média final** obtida, **conceito correspondente** e o **respectivo resultado**. Se o usuário informar para qualquer uma das notas valores fora do intervalo permitido $0 \leq nota \leq 100$, o programa deve gerar como saída o texto **NOTA INVÁLIDA**.


#python
nota1 = int(input("Digite a primeira nota (0 a 100): "))
nota2 = int(input("Digite a segunda nota (0 a 100): "))
nota3 = int(input("Digite a terceira nota (0 a 100): "))

if not (0 <= nota1 <= 100) or not (0 <= nota2 <= 100) or not (0 <= nota3 <= 100):
    print("NOTA INVÁLIDA")
else:
    media = (nota1 * 0.2) + (nota2 * 0.3) + (nota3 * 0.5)

    if 0 <= media and media <= 20:
        conceito = 'E'
        resultado = 'REPROVADO'
    elif 21 <= media <= 40:
        conceito = 'D'
        resultado = 'REPROVADO'
    elif 41 <= media <= 60:
        conceito = 'C'
        resultado = 'EXAME'
    elif 61 <= media <= 80:
        conceito = 'B'
        resultado = 'APROVADO'
    elif 81 <= media <= 100:
        conceito = 'A'
        resultado = 'APROVADO'

    print(f"Média final: {media:.1f}")
    print(f"Conceito: {conceito}")
    print(f"Resultado: {resultado}")


### Exercício 4

#FUAQ(*faça um algoritmo que*) receba três valores do usuário, esses valores são referentes ao tamanho de retas de um triângulo.
#De acordo com as medidas recebidas informe para o usuário se as medidas são de um Triângulo isósceles, equilatero ou escaleno.

#🔺 Triângulo Equilátero - Todos os lados têm a mesma medida

#🔺 Triângulo Isósceles - Dois lados iguais e um lado diferente

#🔺 Triângulo Escaleno - Todos os lados são diferentes

#python
# Recebe os três lados do triângulo
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if lado1 == lado2 == lado3:
    tipo = "Triângulo Equilátero"
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    tipo = "Triângulo Isósceles"
else:
    tipo = "Triângulo Escaleno"

print(f"Tipo: {tipo}")

### Exercício 5

#O calendário gregoriano introduziu o conceito de ano bissexto como uma forma de corrigir, a cada 4 anos, a diferença  de tempo entre o ano sideral (tempo de translação da Terra em torno do Sol) e o tempo de um ano do calendário. Em anos bissextos, o calendário é acrescido de 1 dia (24 horas).

#Podemos determinar se um ano é bissexto através de cálculos de resto de divisão inteira. Todo ano bissexto deve atender às seguintes condições:

# Se 400 for um divisor do ano, então é bissexto;
# Ou, se o ano for divisível por 4, mas não por 100, ele é considerado bissexto.

#Sabendo os critérios para identificar anos bissextos, iremos agora desenvolver um programa que fará este trabalho para nós. Basta que este programa solicite ao usuário o ano e, como saída, informar uma das mensagens abaixo, a depender do resultado.

# **BISSEXTO**
# **NÃO É BISSEXTO**
# **ANO INVÁLIDO** (caso seja informado valor igual ou inferior a zero)

# python
ano = int(input("Digite o ano (maior que 0): "))

if ano <= 0:
    print("Digite um valor válido")
else:
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        print("BISSEXTO")
    else:
        print("NÃO É BISSEXTO")

### Exercício 6

#Leia a idade de um nadador e escreva em tela a respectiva categoria em que se enquadra. Os intervalos de idade estão descritos na tabela que segue.

#| Categoria  | Faixa etária       |
#| ---------- | ------------------ |
#| infantil A | 5 - 7 anos         |
#| infantil B | 8 - 10 anos        |
#| juvenil A  | 11 - 13 anos       |
#| juvenil B  | 14 - 17 anos       |
#| adulto     | maiores de 18 anos |


# python
idade = int(input("Informe a idade do nadador: "))

# Verifica a categoria com base na idade
if 5 <= idade <= 7:
    categoria = "infantil A"
elif 8 <= idade <= 10:
    categoria = "infantil B"
elif 11 <= idade <= 13:
    categoria = "juvenil A"
elif 14 <= idade <= 17:
    categoria = "juvenil B"
elif idade >= 18:
    categoria = "adulto"
else:
    categoria = "Idade fora das categorias"

print(f"Categoria: {categoria}")

### Exercício 7

# Um engenheiro deseja construir uma base quadrada para uma torre de observação.

# FUAQ que receba dois valores sendo o tamanho dos lados de um quadrado em metros e encontre a área desse quadrado.

#🟩  Lembrete: a área do quadrado é calculada pela fórmula:
#A = lado × lado

lado = float(input("Informe o tamanho do lado do quadrado (em metros): "))

area = lado * lado  # ou: area = lado ** 2

print(f"A área do quadrado é {area:.2f} metros quadrados.")

### Exercício 8

a = 5
b = 10
c = 15

if a < b and b < c:
    print("Ordem crescente")
elif a > b and b > c:
    print("Ordem decrescente")
else:
    print("Ordem indefinida")


# Qual será a saída do programa?

# A. **Ordem crescente**
# B. Ordem decrescente
# C. Ordem indefinida
# D. Erro de sintaxe
# E. Nenhuma opção acima

### Exercício 9

# Um caixa eletrônico está programado para não permitir saques inferiores a R$ 10 ou superiores a R$ 1000, e só permite saques múltiplos de 10.

#FUAQ Escreva um trecho que leia o valor desejado e imprima:

# "Saque autorizado" se for válido
# "Valor inválido" caso contrário


valor = int(input("Digite o valor do saque: "))

if valor >= 10 and valor <= 1000 and valor % 10 == 0:
    print("Saque autorizado")
else:
    print("Valor inválido")



### Exercício 10

dia = input("Digite o dia da semana: ").lower()

match dia:
    case "segunda":
        print("Início da semana útil")
    case "sexta":
        print("Último dia útil")
    case "sábado" | "domingo":
        print("Final de semana")
    case _:
        print("Dia inválido")
