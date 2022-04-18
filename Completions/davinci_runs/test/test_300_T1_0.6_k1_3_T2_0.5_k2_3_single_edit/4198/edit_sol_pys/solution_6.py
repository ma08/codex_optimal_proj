

def main():
    A, B, X = map(int, input().split())
    if X <= A + B:
        print(0)
    else:
        left = 0
        right = 10 ** 9
        mid = (left + right) // 2
        while A * mid + B * len(str(mid)) <= X:
            left = mid
            mid = (left + right) // 2
        print(left)

if __name__ == '__main__':
    main()
