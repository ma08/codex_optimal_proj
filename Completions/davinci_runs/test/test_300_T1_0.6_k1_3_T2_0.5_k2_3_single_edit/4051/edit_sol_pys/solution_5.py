

def main():
    n = int(input())
    arr = list(map(int, input().split()))[:n]

    stack = []

    for i in arr:
        stack.append([i for j in range(i)])

    stack = [j for i in stack for j in i]
    stack.sort()
    print(stack)

    for i in range(1, len(stack)):
        if stack[i] - stack[i-1] > 1:
            print("NO")
            break
    else:
        print("YES")


main()
