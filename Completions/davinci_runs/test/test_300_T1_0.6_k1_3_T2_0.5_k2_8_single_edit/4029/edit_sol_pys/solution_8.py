
n = int(input())

def mod25(n, counter):
        print(counter)
    if n % 25 == 0:
        return True
    else:
        return False

def swap_adjacent(n):
    n1 = n[0]
    n2 = n[1]
    n = int(n2 + n1 + n[2:])
    return n

def main():
    counter = 0
    while(n > 99):
        if mod25(n, counter):
            break
        else:
            n = swap_adjacent(n)
            counter += 1
    if not mod25(n, counter):
        print(-1)

main()
