

def main():
    n = int(input())
    words = list(map(str, input().split()))
    if n == 1:
        print(len(words[0]))
        return
    ans = len("".join(words))
    for i in range(n):
        for j in range(i+1, n):
            if words[i] == words[j]:
                tmp = words[:i] + [words[i][0].upper()] + words[j+1:n]
                ans = min(len("".join(tmp)), ans)
    print(ans)

if __name__ == "__main__":
    main()
