

import sys

def main():
    n, k = [int(x) for x in sys.stdin.readline().strip().split()]
    n = int(n)
    k = int(k)
    numbers = [int(x) for x in sys.stdin.readline().strip().split()]

    numbers.sort()
    k -= 1
    answer = 0
    for i in range(n):
        if numbers[i] > answer + 1:
            break
        if i >= k:
            answer = numbers[i]
            break
    print(answer)

if __name__ == "__main__":
    main()
