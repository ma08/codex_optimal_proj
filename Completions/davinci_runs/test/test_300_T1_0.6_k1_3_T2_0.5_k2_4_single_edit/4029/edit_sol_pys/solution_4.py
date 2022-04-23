

n = int(input())

def mod25(n):
    if n % 25 == 0:
        return True
    else:
        return False

def swap_adjacent(n):
    n = str(n)
    n1 = int(n[0])
    n2 = int(n[1])
    n = str(n2) + str(n1) + n[2:]
    return int(n)

def main():
    counter = 0
    while(len(str(n)) > 2):
        if mod25(n):
            break
        else:
            n = swap_adjacent(n)
            counter += 1
    if mod25(n):
        print(counter)
    else:
        print(-1)

main()
