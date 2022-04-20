

N = int(input())

def get_name(n):
    name = ''
    while n > 0:
        name = chr(97 + n % 26) + name
        n = n // 26 - 1
    return name

print(get_name(N-1))
