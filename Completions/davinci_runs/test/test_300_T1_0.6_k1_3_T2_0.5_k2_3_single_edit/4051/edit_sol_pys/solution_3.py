

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    stack = []

    for i in range(n):
        stack.append([i+1 for j in range(arr[i])])

    stack = [item for sublist in stack for item in sublist]

    stack.sort()

    for i in range(len(stack)):
        if i == len(stack) - 1:
            print("YES")
        elif stack[i+1] - stack[i] > 1:
            print("NO")
            break


main()
