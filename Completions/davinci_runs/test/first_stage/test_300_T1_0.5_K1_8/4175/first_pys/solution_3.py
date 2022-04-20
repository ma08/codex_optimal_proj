

def main():
    N = int(input())
    words = []
    for i in range(N):
        word = input()
        if i > 0 and word[0] != words[i-1][-1]:
            print("No")
            return
        if word in words:
            print("No")
            return
        words.append(word)
    print("Yes")

if __name__ == '__main__':
    main()