

def main():
    n = int(input())
    arr = list(map(int, input().split()))[:n]

    stack = [0] * n

    for i in range(n):
        stack[i] = arr[i]

    stack.sort()

    for i in range(1, len(stack)):
        if stack[i] - stack[i-1] > 1:
            print("NO")
            break
    else:
        print("YES")


main()
