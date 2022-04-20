

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if max(a) - min(a) > 1:
        print("NO")
        return
    if max(a) - min(a) == 1:
        if a.count(max(a)) > 1 and a.count(min(a)) > 1:
            print("NO")
            return
    print("YES")

if __name__ == '__main__':
    main()