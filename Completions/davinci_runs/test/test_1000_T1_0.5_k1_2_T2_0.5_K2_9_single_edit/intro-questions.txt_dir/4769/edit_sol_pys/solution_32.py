

def main():
    s = input()
    if len(s) % 2 == 1:
        print(-1)
    else:
        half = len(s) // 2
        first = s[:half]
        second = s[half:]
        first_letters = {}
        second_letters = {}
        for letter in first:
            if letter in first_letters:
                first_letters[letter] += 1
            else:
                first_letters[letter] = 1
        for letter in second:
            if letter in second_letters:
                second_letters[letter] += 1
            else:
                second_letters[letter] = 1
        for key in first_letters:
            if key not in second_letters:
                print(-1)
            elif first_letters[key] != second_letters[key]:
                print(-1)
        print(first)


if __name__ == "__main__":
    main()
