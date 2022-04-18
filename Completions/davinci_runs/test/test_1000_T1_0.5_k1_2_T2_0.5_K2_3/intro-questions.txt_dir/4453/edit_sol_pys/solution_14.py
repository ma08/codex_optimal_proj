

def main():
    q = int(input())
    for i in range(q):
        n,m = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]
        count = 0
        for j in range(m):
            if a[j] != b[j]:
                count += 1
                for k in range(j+1,m):
                    if a[k] == b[j]:
                        count += k-j
                        a = a[:j] + a[k:j:-1] + a[j+1:k] + a[k+1:]
                        break
        print(count)

main()
