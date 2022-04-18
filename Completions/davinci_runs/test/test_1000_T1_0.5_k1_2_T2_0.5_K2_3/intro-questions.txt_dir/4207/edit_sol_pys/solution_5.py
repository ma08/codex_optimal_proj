
def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]    
    a = sorted(a)
    b = sorted(b)
    count = 0
    for i in range(n//2):
        if a[i] < b[i]:
            count += 1
        if a[n-1-i] < b[n-1-i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
