

N = int(input())
divisors = list(map(int, input().split()))

x = divisors[0]
y = divisors[1]
for i in range(N):
    if divisors[i] == divisors[i + 1]:  # if two numbers are equal
        x *= divisors[i]  # then multiply them
        i += 1  # and skip the next number
    else:
        y *= divisors[i]  # otherwise multiply the next number
print(x, y)
