

import sys

def main():
    input = sys.stdin.read().splitlines()
    n = int(input[0])
    a = list(map(int, input[1].split()))
    suma = sum(a)
    nice = []
    for i in range(n):
        if a[i] == suma - a[i]:
            nice.append(i+1)
    print(len(nice))
    print(" ".join(nice))

main()