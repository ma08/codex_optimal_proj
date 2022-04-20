

def calc(words):
    return len("".join(words))

def main():
    n = int(input())
    words = [x for x in input().split()]
    if n == 1:
        print(len(words[0]))
        quit()
    ans = calc(words)
    for i in range(n):
        for j in range(i+1, n):
            if words[i] == words[j]:
                tmp = words[:i] + [words[i][0].upper()] + words[j+1:]
                ans = min(calc(tmp), ans)
    print(ans)

if __name__ == "__main__":
    main()
