

def main():
    n = int(input())
    words = input().split()
    min_length = len("".join(words))

    for i in range(n-1):
        for j in range(i+1, n):
            for k in range(j+1, n+1):
                if words[i:j] == words[j:k]:
                    abbreviation = words[i][0].upper() + str(len(words[i:j]))
                    new_words = words[:i] + [abbreviation] + words[k:]
                    min_length = min(len("".join(new_words)), min_length)
    print(min_length)


if __name__ == '__main__':
    main()