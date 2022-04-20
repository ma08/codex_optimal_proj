

def get_input():
    n = int(input())
    s = input()
    return n, s

def main():
    n, s = get_input()
    stack = []
    count = 0
    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        else:
            if stack == []:
                count += 1
            else:
                stack.pop()
    print(count + len(stack))

if __name__ == '__main__':
    main()