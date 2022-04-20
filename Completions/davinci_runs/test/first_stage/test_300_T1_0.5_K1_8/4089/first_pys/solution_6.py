

n = int(input())

def get_name(n):
    if n <= 26:
        return chr(n + 96)
    else:
        name = ""
        while n > 26:
            name += chr(n % 26 + 96)
            n = n // 26
        name += chr(n + 96)
        return name[::-1]

print(get_name(n))