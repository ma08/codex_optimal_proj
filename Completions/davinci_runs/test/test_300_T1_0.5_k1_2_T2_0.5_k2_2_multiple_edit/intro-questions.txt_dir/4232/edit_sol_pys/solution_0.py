import sys

def main():
    n, k = sys.stdin.readline().strip().split()
    n = int(n)
    k = int(k)
    numbers = [int(x) for x in sys.stdin.readline().strip().split()]
    numbers.sort()
    answer = 0
    for i in range(n):
        if i + 1 >= k:
            answer = numbers[i]
        if numbers[i] > answer + 1:
            break
    if answer == 0:
        print("-1")
    else:
        print(answer)

if __name__ == "__main__":
    main()
