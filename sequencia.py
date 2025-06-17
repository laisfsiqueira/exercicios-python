# soma dos inversos de 1 até 100

S = 0.0  # variável acumuladora

# Loop de 1 até 100
for i in range(1, 101):
    S += 1 / i

# Imprime o resultado com duas casas decimais
print(f"{S:.2f}")