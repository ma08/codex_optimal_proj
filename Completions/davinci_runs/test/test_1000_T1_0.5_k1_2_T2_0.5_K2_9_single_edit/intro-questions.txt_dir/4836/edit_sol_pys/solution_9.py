

def main():
    n, c = map(int, input().split())  # n = 果物の数, c = 容量
    w = list(map(int, input().split()))  # w = 果物の重さ
    fruits = sorted(w)  # 果物を重さで昇順に並び替える

    i = 0
    total = 0
    while i < n:  # 容量内で収納できるだけ入れる
        if total + fruits[i] <= c:
            total += fruits[i]
            i += 1
        else:
            break

    print(i)

if __name__ == "__main__":
    main()
