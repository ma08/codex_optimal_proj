


def main():
    n = int(input())
    text = input().split()
    text = " ".join(text)

    # find all possible abbrs
    abbrs = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if text[i] == text[j]:
                abbrs.add(text[i:j + 1])

    # find all possible abbrs with 1st letter uppercase
    abbrs_uppercase = set()
    for abbr in abbrs:
        abbrs_uppercase.add(abbr[0].upper() + abbr[1:])

    min_length = len(text)
    for abbr in abbrs_uppercase:
        if text.count(abbr) > 1:
            length = len(text.replace(abbr, abbr[0].upper()))
            if length < min_length:
                min_length = length

    print(min_length)


if __name__ == "__main__":
    main()