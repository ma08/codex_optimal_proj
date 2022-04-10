

import sys

def main():
    input = sys.stdin.read().splitlines()
    n = int(input[0])
    a = list(map(int, input[1].split()))
    sum_ = sum(a)
    nice = []
    for i in range(n):
        if a[i] == sum_ - a[i]:
            nice.append(i+1)
    print(len(nice))
    print(" ".join(map(str, nice)))

main()
