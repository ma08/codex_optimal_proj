

def main():
    a, b, x = map(int, input().split())
    #B = B * 9
    #print(A, B, X)
    if x <= a + b:
        print(0)
    else:
        left = 0
        right = 10 ** 9
        while left + 1 < right:
            mid = (left + right) // 2
            if a * mid + b * len(str(mid)) <= x:
                left = mid
            else:
                right = mid
        print(left)

if __name__ == '__main__':
    main()
