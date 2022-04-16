
def shift(c, k, i):
    return chr((ord(c) - ord('A') + (ord(k[i]) - ord('A')) * (-1) ** i) % 26 + ord('A'))
c = input().strip()
k = input().strip()
print("".join(shift(c[i], k, i) for i in range(len(c)))
