

def next_day(a):
    n = len(a)
    for i in range(n-1):
        if a[i] == a[i+1]:
            a[i] += 1
            a[i+1] += 1
    return a

def possible(a):
    if len(set(a)) == 1:
        return "YES"
    else:
        return "NO"

def main():
    n = int(input())
    a = list(map(int, input().split())
    for i in range(n*n):
        a = next_day(a)
        if possible(a):
            print(possible(a))
            break

if __name__ == '__main__':
    main()
