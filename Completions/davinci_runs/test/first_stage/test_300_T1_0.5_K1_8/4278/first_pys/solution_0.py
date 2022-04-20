

def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    words.sort()
    count = 0
    for i in range(n-1):
        if words[i] == words[i+1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()