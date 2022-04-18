

def main(n, m, d):
    if m == 0:
        print(" ".join(map(str,range(1,n+1))))
    else:
        result = [1]
        for i in d:
            result.insert(i, len(result) + 1)
        print(" ".join(map(str,result)))

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    d = list(map(int, input().split()))
    main(n,m,d)
