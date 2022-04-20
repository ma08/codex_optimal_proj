

N = int(input())
# N = 2

def get_name(n):
    if n == 1:
        return 'a'
    else:
        n -= 1
        name = ''
        while n > 0:
            name = chr(97 + n % 26) + name
            n = n // 26 - 1
        return name

print(get_name(N))
