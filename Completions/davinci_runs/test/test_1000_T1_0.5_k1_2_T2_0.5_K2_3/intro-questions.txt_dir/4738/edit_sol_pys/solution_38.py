
s = input()


def is_k_periodic(s, k):
    if len(s) % k != 0:
        return False
    else:
        for i in range(0, len(s) // k):
            if s[i * k] != s[i * k + 1]:
                return False
        return True

k = 1
while not is_k_periodic(s, k):
    k += 1
print(k)
