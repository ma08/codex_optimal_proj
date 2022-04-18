

import sys

def main():
    n, k = sys.stdin.readline().strip().split()
    n = int(n)
    k = int(k) + 1
    numbers = [int(x) for x in sys.stdin.readline().strip().split()]
    numbers.sort()
    answer = 1
    for i in range(n):
        if numbers[i] >= answer + 1:
            break
        if i + 1 >= k - 1:
            answer = numbers[i]
    if answer == 1:
        print("-1")
    else:
        print(answer)

if __name__ == "__main__":
    main()
