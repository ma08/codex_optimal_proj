# 스택을 이용한 풀이

def main():
    string = input().strip()
    stack = []
    for c in string:
        if c == '<':
            if stack:
                stack.pop()
        else:
            stack.append(c)
    print(''.join(stack))

main()
