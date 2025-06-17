N = int(input())

for i in range(N):
  a, b = input().split() #receber dois valores na mesma linha
  if a.endswith(b):
    print("encaixa")
  else:
    print("nao encaixa")