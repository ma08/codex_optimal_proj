

from sys import stdin

def main():
    n = int(stdin.readline())
    lista = stdin.readline()
    lista = list(map(int, lista.split()))
    lista.sort()
    if n % 2 == 0:
        lista.reverse()
    print(" ".join([str(x) for x in lista]))

if __name__ == "__main__":
    main()
