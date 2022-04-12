def unique_count(a):
    a.sort()
    count = 1
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    print(unique_count(a))
