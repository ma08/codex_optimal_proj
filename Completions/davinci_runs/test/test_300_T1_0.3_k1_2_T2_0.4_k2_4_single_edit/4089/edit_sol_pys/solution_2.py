

N = int(input())
# N = 2

def get_name(N):
    if N == 1:
        return 'a'
    else:
        N -= 1
        name = ''
        while N > 0:
            name = chr(97 + N % 26) + name
            N = N // 26 - 1
        return name

print(get_name(N))
