import sys

def main():
    n, k = [int(x) for x in sys.stdin.readline().strip().split()]
    numbers = [int(x) for x in sys.stdin.readline().strip().split()]
    numbers.sort(reverse=True)
    answer = 0
    for i in range(n):
        if numbers[i] > answer + 1:
            break
        if i + 1 >= k:  # i + 1 is the number of elements that are greater than or equal to numbers[i]
            answer = numbers[i]
    if answer == 0:
        print("-1")
    else:
        print(answer)

if __name__ == "__main__":
    main()
