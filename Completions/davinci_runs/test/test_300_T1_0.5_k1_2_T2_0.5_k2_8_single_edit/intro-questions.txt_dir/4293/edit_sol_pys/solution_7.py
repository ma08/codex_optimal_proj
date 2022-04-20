

A, B, C, D, E, F = map(int, input().split())

water = [0]
sugar = [0]

for i in range(F+1):
    if i % 100 == 0:
        water.append(i)

for i in range(F+1):
    if i % 100 == 0:
        sugar.append(i)

for i in range(1, F//100+1):
    for j in range(1, F//100+1):
        if i * 100 * A <= F and j * 100 * B <= F:
            water.append(i * 100 * A)
            sugar.append(j * 100 * B)

for i in range(1, F//100+1):
    for j in range(1, F//100+1):
        if i * C + j * D <= F:
            sugar.append(i * C + j * D)

water.sort()
sugar.sort()

max_concentration = 0
max_a = 0
max_b = 0

for i in range(len(water)):
    for j in range(len(sugar)):
        if water[i] + sugar[j] <= F and sugar[j] / (water[i] + sugar[j]) <= E / (100 + E):
            if max_concentration <= sugar[j] / (water[i] + sugar[j]):
                max_concentration = sugar[j] / (water[i] + sugar[j])
                max_a = water[i]
                max_b = sugar[j]

print(max_a + max_b, max_b)
