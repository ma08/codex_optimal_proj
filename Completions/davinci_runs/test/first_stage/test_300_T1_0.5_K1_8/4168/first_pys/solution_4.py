

N = int(input())

res = []
while True:
    if N == 0:
        break
    elif N % 2 == 0:
        res.append(0)
        N //= -2
    else:
        res.append(1)
        N = (N-1) // -2

print(''.join(map(str, res[::-1])))