

def main():
    A, B, X = map(int, input().split())
    if X <= A + B:
        print(0)  # A * 0 + B * 1 <= X
    else:
        left = 0
        right = 10 ** 9 + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A * mid + B * len(str(mid)) <= X:  # mid is ok
                left = mid
            else:  # mid is not ok
                right = mid
        print(left)

if __name__ == '__main__':
    main()
