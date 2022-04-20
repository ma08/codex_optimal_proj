

N = int(input())

def get_name(N):
    if N == 1:
        return "a"
    N -= 1
    name = ""
    while N > 0:
        N -= 1
        name = chr(N % 26 + 97) + name
        N //= 26
    return name

print(get_name(N))