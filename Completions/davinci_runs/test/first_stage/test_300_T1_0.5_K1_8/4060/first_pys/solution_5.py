

# TODO: finish this problem

def main():
    # read input
    n = int(input())
    s = input()

    # find all places where you can flip a bracket to get a valid expression
    ans = 0
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                ans += 1

    if len(stack) > 0:
        ans += len(stack)

    print(ans)

if __name__ == "__main__":
    main()