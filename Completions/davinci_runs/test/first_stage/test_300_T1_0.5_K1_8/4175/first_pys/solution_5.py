

def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for i in range(n - 1):
        if words[i] == words[i + 1] or words[i][-1] != words[i + 1][0]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()