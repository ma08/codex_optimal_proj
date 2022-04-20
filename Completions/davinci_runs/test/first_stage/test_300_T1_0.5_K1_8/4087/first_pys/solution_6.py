

def is_interesting(n):
    n = str(n)
    return int(n) % 4 == 0

def nearest_interesting(n):
    while not is_interesting(n):
        n += 1
    return n

print nearest_interesting(int(raw_input()))