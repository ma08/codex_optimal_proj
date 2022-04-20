

import sys

def main():
    n = int(sys.stdin.readline().strip())
    a = [int(i) for i in sys.stdin.readline().strip().split()]

    if n == 2:
        print("{} {}".format(max(a), min(a)))
        return

    for i in range(n):
        for j in range(i+1, n):
            if a[j] % a[i] == 0 and a[j] / a[i] in [2, 3]:
                a[j], a[i] = a[i], a[j]
                break
    print(" ".join([str(i) for i in a]))

if __name__ == "__main__":
    main()