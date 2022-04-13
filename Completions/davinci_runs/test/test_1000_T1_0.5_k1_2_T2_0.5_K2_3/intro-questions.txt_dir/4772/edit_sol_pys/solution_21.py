

def main():
    n, m = [int(i) for i in input().split()]
    puzzle = [input() for _ in range(n)]
    words = set()
    for i in range(n):
        word = ''
        for j in range(m):
            if puzzle[i][j].isalpha():
                word += puzzle[i][j]
            else:
                if len(word) > 1:
                    words.add(word)
                word = ''
        if len(word) > 1:
            words.add(word)
    for j in range(m):
        word = ''
        for i in range(n):
            if puzzle[i][j].isalpha():
                word += puzzle[i][j]
            else:
                if len(word) > 1:
                    words.add(word)
                word = ''
        if len(word) > 1:
            words.add(word)
    print(min(words))

if __name__ == '__main__':
    main()
