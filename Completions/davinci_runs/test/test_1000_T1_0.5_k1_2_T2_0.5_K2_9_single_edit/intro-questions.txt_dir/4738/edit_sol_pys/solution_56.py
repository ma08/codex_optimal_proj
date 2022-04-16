
s = input()


def is_k_periodic(s, k):
    if len(s) % k != 0:
        return False
    else:
        for i in range(1, len(s)//k):
            if s[i*k-1] != s[i*k:]:
                return False
        return True

k = 1
while not is_k_periodic(s, k):
    k += 1
print(k)
