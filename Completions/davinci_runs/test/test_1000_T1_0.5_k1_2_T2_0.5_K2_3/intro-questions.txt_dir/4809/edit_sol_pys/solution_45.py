
def coconut_splitter(s, n):
    if s%2 == 0:
        return (n - 1) % 2 + 1
    else:
        return (n - 1) % 3 + 1

print(coconut_splitter(9, 4))
