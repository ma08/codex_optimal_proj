
def main():
    n = int(input())
    s = input()
    t = input()
    moves = []
    for i in range(n):
        if s[i] != t[i]:
            for j in range(i + 1, n):
                if s[j] == t[i]:
                    s = s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]
                    moves.append(i)
                    break
            else:
                print(-1)
                return
    print(len(moves))
    print(*moves, sep="\n")

if __name__ == "__main__":
    main()
