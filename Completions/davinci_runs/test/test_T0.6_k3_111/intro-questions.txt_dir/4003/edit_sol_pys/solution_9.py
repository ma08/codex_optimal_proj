
def main():
    n = int(input())
    a = list(map(int, input().split()))
    left = []
    right = []
    answer = []
    while a:
        if not left:
            left.append(a.pop(0))
            answer.append('L')
        elif not right:
            right.append(a.pop())
            answer.append('R')
        elif left[-1] < right[-1]:
            right.append(a.pop())
            answer.append('R')
        elif left[-1] < a[0]:
            left.append(a.pop(0))
            answer.append('L')
        elif right[-1] < a[-1]:
            right.append(a.pop())
            answer.append('R')
        else:
            break
    print(len(left) + len(right), ''.join(answer))


if __name__ == '__main__':
    main()
