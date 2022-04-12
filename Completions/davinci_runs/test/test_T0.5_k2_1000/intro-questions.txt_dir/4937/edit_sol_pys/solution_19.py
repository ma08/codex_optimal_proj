

def main():
    n, a = map(int, input().split())  # n:個数 a:重さ
    e = list(map(int, input().split()))  # e:重さリスト
    e.sort()  # ソート
    count = 0
    for i in range(n):
        if a >= e[i]:
            a -= e[i]
            count += 1
        else:
            break
    print(count)

main()
