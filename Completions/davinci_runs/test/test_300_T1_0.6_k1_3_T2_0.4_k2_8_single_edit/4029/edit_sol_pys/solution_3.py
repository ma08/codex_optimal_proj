

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

    n = int(input())
def main():
    n = str(n)
    counter = 0
    while(len(n) > 2):
        if mod25(int(n)):
            break
        else:
            n = swap_adjacent(n)
            counter += 1
    if mod25(int(n)):
        print(counter)
    else:
        print(-1)

main()
