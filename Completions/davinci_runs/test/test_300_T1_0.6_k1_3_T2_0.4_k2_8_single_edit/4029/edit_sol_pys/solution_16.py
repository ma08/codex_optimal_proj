
n = int(input())

def swap_adjacent(n):
    n = list(str(n))
    n[0], n[1] = n[1], n[0]
    return int(''.join(n))

def main():
    n = str(n)
    counter = 0
    while(len(n) > 2):
        if int(n) % 25 == 0:
            break
        else:
            n = swap_adjacent(n)
            counter += 1
    if int(n) % 25 == 0:
        print(counter)
    else:
        print(-1)

main()
