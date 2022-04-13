from collections import deque


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        num_of_operations = int(input())
        queue = deque()
        for _ in range(num_of_operations):
            operation = input().split()
            if operation[0] == '1':
                queue.append(operation[1])
            elif operation[0] == '2':
                queue.popleft()
            else:
                print(queue[0])

if __name__ == "__main__":
    main()
