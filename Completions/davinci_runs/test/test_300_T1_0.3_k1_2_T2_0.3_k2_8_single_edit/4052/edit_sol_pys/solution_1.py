

def main():
    n = int(input())
    s = input()
    t = input()
    moves = 0
    for i in range(n):
        if s[i] != t[i]:
            for j in range(i+1, n):
                if s[j] == t[i]:
                    moves += 1
                    s = s[:j] + s[j+1] + s[j] + s[j+2:]
                    break
    if s == t:
        print(moves)
    else:
        print(-1)

if __name__ == '__main__':
    main()
