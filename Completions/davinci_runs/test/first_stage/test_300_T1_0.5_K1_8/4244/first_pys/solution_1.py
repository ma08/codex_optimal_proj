

N = int(input())
X = [int(i) for i in input().split()]

min_stamina = 10**10
for i in range(1,101):
    total = 0
    for j in X:
        total += (j - i)**2
    if total < min_stamina:
        min_stamina = total
print(min_stamina)