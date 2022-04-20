
n = int(input())

def mod25(n):
    if n % 25 == 0:
        return True
    else:
        return False

def swap_adjacent(n):
    n = str(n)
    n1 = n[0]
    n2 = n[1]
    n = n2 + n1 + n[2:]
    return n

def main():
    if n < 100:
        print(-1)
    else:
        print(-1)

main()
