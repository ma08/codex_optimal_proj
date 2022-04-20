

N = int(input())
X = list(map(int, input().split()))

def calculate_stamina(coordinate, X):
    return sum([(x - coordinate)**2 for x in X])

minimum_stamina = float("inf")
for i in range(min(X), max(X) + 1):
    stamina = calculate_stamina(i, X)
    if stamina < minimum_stamina:
        minimum_stamina = stamina

print(minimum_stamina)