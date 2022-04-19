

def main():
    n = int(input())
    words = [x for x in input().split()]
    if n == 1:
        print(len(words[0]))
        quit()
    ans = len("".join(words))
    for i in range(n):
        for j in range(i+1, n):
            if words[i] == words[j]:
                tmp = words[:i] + [words[i][0].upper()] + words[j+1:] # words[i]とwords[j]をひとつにまとめる
                ans = min(len("".join(tmp)), ans) # 新しい単語列の長さと現在の最小値を比較
    print(ans)

if __name__ == "__main__":
    main()
