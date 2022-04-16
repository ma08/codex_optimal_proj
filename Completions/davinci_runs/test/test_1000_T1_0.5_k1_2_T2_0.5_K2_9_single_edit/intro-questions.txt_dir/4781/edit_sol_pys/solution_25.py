
def main():
    k = int(input()) - 1
    n = int(input())

    for _ in range(n):
        z = input()
        if z == 'T':
            k = (k + 1) % 8 + 1
        elif z == 'N':
            k = (k + 7) % 8 + 1
        else:
            k = (k + 6) % 8 + 1

    print(k)

main()
