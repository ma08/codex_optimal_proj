
# このコードは提出にはならない

def main():
    # 入力
    n, k = map(int, input().split())
    # 文字列をソートしておく
    s = input()

    s = [c for c in s]
    s.sort()
    s = "".join(s)

    curr = s[0]
    # 同じ文字列が連続する回数を数える
    # 同じ文字列が連続する回数がkを超えると回答は-1
    prev = s[0]
    res = 0
    i = 1
    k_count = 0
    while i < len(s):
        if s[i] != prev:
            if k_count + len(curr) > k:
                print(-1)
                return
            k_count += len(curr)
            curr = ""
        prev = s[i]
        curr += s[i]
        i += 1
    if k_count + len(curr) > k:
        print(-1)
        return

    # 同じ文字列が連続する回数を数える
    # 同じ文字列が連続する回数がkを超えると回答は-1
    curr = s[0]
    prev = s[0]
    res = 0
    i = 1
    while i < len(s):
        if s[i] != prev:
            res += len(curr)
            curr = ""
        prev = s[i]
        curr += s[i]
        i += 1
    res += len(curr)

    # 出力
    print(res)

main()
