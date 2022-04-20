

n = int(input())
divisors = [int(x) for x in input().split()]

product = 1
for d in divisors:
    product *= d

possible_divisors = []
for i in range(1, int(product ** 0.5) + 1):
    if product % i == 0:
        possible_divisors.append(i)
        possible_divisors.append(int(product / i))
possible_divisors = sorted(possible_divisors)

possible_divisors = set(possible_divisors)
divisors_for_x = [divisors[0]]
possible_divisors.remove(divisors[0])

for d in divisors[1:]:

    if d in possible_divisors:
        possible_divisors.remove(d)
        divisors_for_x.append(d)
    else:
        possible_divisors.remove(product // d)

divisors_for_y = [d for d in possible_divisors]

x = 1
y = 1
for d in divisors_for_x:
    x *= d
for d in divisors_for_y:
    y *= d

print(x, y)
