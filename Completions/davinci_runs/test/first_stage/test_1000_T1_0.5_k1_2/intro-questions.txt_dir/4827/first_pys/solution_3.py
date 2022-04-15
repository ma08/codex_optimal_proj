

def main():
    # Read the number of words
    N = int(input())

    # Read the words
    words = []
    for i in range(N):
        words.append(input())

    # Find the position of the $
    position = words.index("$")

    # Calculate the number of letters
    number_of_letters = 0
    for i in range(N):
        if i != position:
            number_of_letters += len(words[i])

    # Write the output
    for i in range(N):
        if i == position:
            print(name(number_of_letters), end=" ")
        else:
            print(words[i], end=" ")
    print()

def name(number):
    """
    Returns the English name of the number.
    """
    if number == 0:
        return "zero"
    elif number == 1:
        return "one"
    elif number == 2:
        return "two"
    elif number == 3:
        return "three"
    elif number == 4:
        return "four"
    elif number == 5:
        return "five"
    elif number == 6:
        return "six"
    elif number == 7:
        return "seven"
    elif number == 8:
        return "eight"
    elif number == 9:
        return "nine"
    elif number == 10:
        return "ten"
    elif number == 11:
        return "eleven"
    elif number == 12:
        return "twelve"
    elif number == 13:
        return "thirteen"
    elif number == 14:
        return "fourteen"
    elif number == 15:
        return "fifteen"
    elif number == 16:
        return "sixteen"
    elif number == 17:
        return "seventeen"
    elif number == 18:
        return "eighteen"
    elif number == 19:
        return "nineteen"
    elif number == 20:
        return "twenty"
    elif number == 30:
        return "thirty"
    elif number == 40:
        return "forty"
    elif number == 50:
        return "fifty"
    elif number == 60:
        return "sixty"
    elif number == 70:
        return "seventy"
    elif number == 80:
        return "eighty"
    elif number == 90:
        return "ninety"
    elif number <= 99:
        return name(number // 10 * 10) + name(number % 10)
    elif number == 100:
        return "onehundred"
    elif number == 200:
        return "twohundred"
    elif number == 300:
        return "threehundred"
    elif number == 400:
        return "fourhundred"
    elif number == 500:
        return "fivehundred"
    elif number == 600:
        return "sixhundred"
    elif number == 700:
        return "sevenhundred"
    elif number == 800:
        return "eighthundred"
    elif number == 900:
        return "ninehundred"
    elif number <= 999:
        return name(number // 100 * 100) + name(number % 100)
    else:
        return ""

if __name__ == "__main__":
    main()