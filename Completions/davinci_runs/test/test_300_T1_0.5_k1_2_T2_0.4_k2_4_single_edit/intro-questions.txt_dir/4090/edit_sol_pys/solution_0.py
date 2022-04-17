

def main():
    n = int(input())
    words = [x for x in input().split()]
    if n == 1:
        print(len(words[0]))
        quit()
    ans = len("".join(words)) + 1
    for i in range(n):
        for j in range(i+1, n):
            if words[i] == words[j]:
                tmp = words[:i] + [words[i][0].upper()] + words[i+1:j] + words[j+1:]
                ans = min(len("".join(tmp)), ans)
    print(ans)

if __name__ == "__main__":
    main()
