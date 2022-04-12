

def coconut_splitter(s, n):
    return (n - 1) % s + 1

s, n = map(int, input().split())
print(coconut_splitter(s, n))
