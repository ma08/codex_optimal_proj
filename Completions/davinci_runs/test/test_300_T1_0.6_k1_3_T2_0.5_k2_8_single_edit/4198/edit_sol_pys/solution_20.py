

def main():
    A, B, X = map(int, input().split())
    if X <= A + B:
        print(0)
    else:
        left = 0
        right = 10 ** 9
        while left + 1 < right:
            mid = (left + right) // 2
            if A * mid + B * len(str(mid)) <= X:
                left = mid
            else:
                right = mid
        print(left) 

if __name__ == '__main__':
    main()
