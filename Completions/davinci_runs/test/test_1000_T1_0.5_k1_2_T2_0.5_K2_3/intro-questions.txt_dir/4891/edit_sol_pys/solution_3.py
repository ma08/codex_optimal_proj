# Counting sheep

def count_sheep(n):
    if n == 0:
        return "INSOMNIA"
    else:
        digits = set()
        i = 1
        while len(digits) < 10:
            digits = digits.union(set(str(i * n)))
            i += 1
        return (i - 1) * n

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    print("Case #{}: {}".format(i, count_sheep(n)))
