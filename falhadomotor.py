n = int(input())
achou = False

lista = list(map(int, input().split()))
for i in range (1, len(lista)):
  if lista[i] < lista[i-1]:
    print(i+1)
    achou = True
    break
if (not achou):
  print("0")