import sys
import itertools


N = int(sys.stdin.readline())
numbers = [int(x) for x in sys.stdin.readline().split()]
numbers.sort()

def main():
    if len(numbers) == 1:
        print(numbers[0])
        return
    if len(numbers) == 2:
        print(numbers[1])
        return

    m = numbers[-1]
    numbers.pop()
    n = numbers[-1]
    numbers.pop()

    if m < 2*n:
        numbers.append(m+n)
        numbers.sort()
    else:
        numbers.append(m)
    main()

    print(numbers)

main()
