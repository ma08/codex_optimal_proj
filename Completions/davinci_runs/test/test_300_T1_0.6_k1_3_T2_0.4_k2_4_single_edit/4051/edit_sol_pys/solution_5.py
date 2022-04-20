

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    stack = []

    for i in range(n):
        stack.append([i+1 for j in range(arr[i])])

    stack = [item for sublist in stack for item in sublist]

    stack.sort(reverse=True)

    for i in range(len(stack) - 1):
        if stack[i] - stack[i+1] > 1:
            print("NO")
            break
        elif stack[i] - stack[i+1] == 1:
            continue
            break
    else:
        print("YES")


main()
