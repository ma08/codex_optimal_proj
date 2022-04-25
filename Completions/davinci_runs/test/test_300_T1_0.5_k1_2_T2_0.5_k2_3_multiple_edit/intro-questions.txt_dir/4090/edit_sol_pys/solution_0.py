

def main():
    words = [x for x in input().split()]
    n = int(input())
    words.sort()
    if n == 1:
        print(len(words[0]))
        quit()
    if len(words) == len(set(words)):
        print(len("".join(words)))
        quit()
    ans = len("".join(words))
    for i in range(n):
        for j in range(i+1, n):
            if words[i] == words[j]:
                tmp = words[:i] + [words[i][0].upper()] + words[j+1:]
                ans = min(len("".join(tmp)), ans)
    print(ans)

if __name__ == "__main__":
    main()
