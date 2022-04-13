

def main():
    k = int(input())
    n = int(input())

    for _ in range(n):
        t, z = input().split()
        t, z = int(t), z
        if z == 'T':
            k = (k + t) % 8
        elif z == 'S':
            k = (k + 8 - t) % 8
        else:
            k = (k + 8 + t) % 8

    print(k)

main()
