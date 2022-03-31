

def main():
    n = int(input())
    words = input().split(' ')
    count = {}
    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    freq = 0
    for word, num in count.items():
        if num > freq:
            freq = num
    print(len(words) - freq + 1)

if __name__ == "__main__":
    main()
