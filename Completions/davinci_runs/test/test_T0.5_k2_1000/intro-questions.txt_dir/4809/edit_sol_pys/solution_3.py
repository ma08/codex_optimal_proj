

def coconut_splitter(s, n, k):
    return (n - 1) % k + 1

s, n, k = map(int, input().split())
print(coconut_splitter(s, n, k))
