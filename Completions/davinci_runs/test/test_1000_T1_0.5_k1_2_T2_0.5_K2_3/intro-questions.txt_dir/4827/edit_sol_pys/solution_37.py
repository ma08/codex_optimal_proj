

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
    for i in range(N-1):
        if i != position:
            number_of_letters += len(words[i])

    # Write the output
    for i in range(N-1):
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
        return "one hundred"
    elif number == 200:
        return "two hundred"
    elif number == 300:
        return "three hundred"
    elif number == 400:
        return "four hundred"
    elif number == 500:
        return "five hundred"
    elif number == 600:
        return "six hundred"
    elif number == 700:
        return "seven hundred"
    elif number == 800:
        return "eight hundred"
    elif number == 900:
        return "nine hundred"
    elif number <= 999:
        return name(number // 100 * 100) + name(number % 100)
    else:
        return ""

if __name__ == "__main__":
    main()
