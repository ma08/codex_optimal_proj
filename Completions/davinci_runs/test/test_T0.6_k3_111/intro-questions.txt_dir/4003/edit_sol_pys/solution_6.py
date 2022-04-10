from collections import deque


def main():
    n = int(input())
    a = list(map(int, input().split()))
    l = deque()
    r = deque()
    ans = []
    while a:
        if not l:
            l.append(a.pop(0))  # pop(0) is O(n)
            ans.append('L')
        elif not r:
            r.append(a.pop())  # pop() is O(1)
            ans.append('R')
        elif l[-1] < r[0]:
            r.appendleft(a.pop())
            ans.append('R')
        elif l[-1] < a[0]:
            l.append(a.pop(0))
            ans.append('L')
        elif r[-1] < a[-1]:
            r.appendleft(a.pop())
            ans.append('R')
        else:
            break
    print(len(l) + len(r))
    print(''.join(ans))


if __name__ == '__main__':
    main()
