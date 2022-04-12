
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:n]
    a.sort()
    b.sort(reverse=True)
    for i in range(k):
        if a[i] < b[i]:
            a[i] = b[i]
        else:
            break
    print(sum(a))

if __name__ == '__main__':
    main()
