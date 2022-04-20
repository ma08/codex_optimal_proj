

import sys

def main(n, k, numbers):
    numbers.sort()
    answer = -1
    for i in range(n - k + 1):
        if numbers[i + k - 1] - numbers[i] + 1 < answer or answer == -1:
            answer = numbers[i + k - 1] - numbers[i] + 1
    return answer

if __name__ == "__main__":
    n, k = sys.stdin.readline().strip().split()
    n = int(n)
    k = int(k)
    numbers = [int(x) for x in sys.stdin.readline().strip().split()]
    print(main(n, k, numbers))
