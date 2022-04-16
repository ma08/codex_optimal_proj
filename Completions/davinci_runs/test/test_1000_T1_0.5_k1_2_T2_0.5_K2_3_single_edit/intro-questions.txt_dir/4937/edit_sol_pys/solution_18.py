

def main():
    n, a = map(int, input().split()) # n: 人数, a: カロリー
    e = list(map(int, input().split())) # e: エネルギー
    e.sort()
    i = 0
    while a > 0 and i < n:
        if a >= e[i]:
            a -= e[i]
            i += 1
        else:
            break
    print(i)

if __name__ == "__main__":
    main()
