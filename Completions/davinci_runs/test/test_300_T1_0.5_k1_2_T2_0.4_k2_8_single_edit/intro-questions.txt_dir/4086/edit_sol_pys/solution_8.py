from collections import deque

def main():
    n = int(input())
    numbers = deque()
    for _ in range(n):
        numbers.append(int(input()))
    numbers = list(dict.fromkeys(numbers))
    print(len(numbers))
    print(*numbers)

main()
