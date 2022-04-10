

def is_diverse(word):
    if len(word) != len(set(word)):
        return False
    else:
        start = ord(word[0])
        for i in range(1, len(word)):
            if ord(word[i]) != start + i:
                return False
        return True

def main():
    num_words = int(input())
    for _ in range(num_words):
        word = input()
        if is_diverse(word):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()