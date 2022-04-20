

def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    s.sort(key=len)
    for i in range(n):
        for j in range(i+1, n):
            if s[i] not in s[j]:
                print('NO')
                return
    print('YES')
    for i in s:
        print(i)

main()