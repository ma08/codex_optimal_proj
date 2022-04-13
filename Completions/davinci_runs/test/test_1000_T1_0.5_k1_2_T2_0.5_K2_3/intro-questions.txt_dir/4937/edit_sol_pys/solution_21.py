

def main():
    n, a = map(int, input().split()) # n: 人数, a: 合計金額
    e = sorted(list(map(int, input().split()))) # e: 各人が持っている金額
    count = 0
    for i in range(n):
        if a >= e[i]:
            a -= e[i]
            count += 1
        else:
            break
    print(count)

main()
