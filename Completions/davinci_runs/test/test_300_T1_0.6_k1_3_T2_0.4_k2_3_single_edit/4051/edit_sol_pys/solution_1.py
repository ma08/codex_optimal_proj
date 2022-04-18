

def main():
    n = int(input())  # number of students
    arr = list(map(int, input().split()))  # number of submissions

    stack = []  # stack of submissions

    for i in range(n):
        stack.append([i+1 for j in range(arr[i])])

    # filling stack
    stack = [item for sublist in stack for item in sublist]

    stack.sort()
    # flattening stack


    # sorting stack
    for i in range(len(stack) - 1):
        if stack[i+1] - stack[i] > 1:  # if difference between submissions is more than 1
            print("NO")
            break
    else:  # if all submissions are in order
        print("YES")


main()
