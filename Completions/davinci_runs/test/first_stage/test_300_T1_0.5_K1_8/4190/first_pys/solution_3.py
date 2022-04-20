

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [(a[i] + b[i]) % n for i in range(n)]
    d = {i:[] for i in range(n)}
    for i in range(n):
        d[c[i]].append(b[i])
    for i in range(n):
        d[i].sort()
    for i in range(n):
        for j in range(len(d[i])):
            print(d[i][j], end=" ")

main()