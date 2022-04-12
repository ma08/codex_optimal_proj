

def main():
    n = int(input())
    a = [int(i) for i in input().split()]  # a[i] = a_i
    b = [int(i) for i in input().split()]  # b[i] = b_i
    
    if a == [0] * n:
        print(0)
        return
    if b == [0] * n:
        print(n)
        return
    
    a.sort()
    b.sort()
    ans = 0
    for i in range(n):
        if a[i] * b[n - 1 - i] > 0:
            break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
