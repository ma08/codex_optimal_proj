

def main():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:n]
    a_count = 0
    b_count = 0
    for i in range(n):
        if a[i] > b[i]:
            a_count += a[i] - b[i]
        elif a[i] < b[i]:
            b_count += b[i] - a[i]
    if a_count == b_count:
        print('Yes')
    else:
        print('No')

main()
