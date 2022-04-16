

def main():
    n = int(input())
    sentence = []
    for i in range(n):
        word = input()
        if word != "$":
            sentence.append(word)
        else:
            sentence.append("$")
    number = len(sentence) - 1
    number_string = ""
    if number == 0:
        number_string = "zero"
    elif number < 11:
        number_string = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"][number - 1]
    elif number < 20:
        number_string = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][number - 11] + "teen"
    elif number < 100:
        tens_digit = number // 10
        ones_digit = number % 10
        tens_string = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][tens_digit - 2]
        ones_string = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][ones_digit - 1]
        number_string = tens_string
        if ones_digit != 0:
            number_string += "-" + ones_string
    else:
        hundreds_digit = number // 100
        tens_digit = (number % 100) // 10
        ones_digit = (number % 100) % 10
        hundreds_string = ["onehundred", "twohundred", "threehundred", "fourhundred", "fivehundred", "sixhundred", "sevenhundred", "eighthundred", "ninehundred"][hundreds_digit - 1]
        tens_string = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][tens_digit - 2]
        ones_string = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][ones_digit - 1]
        number_string = hundreds_string
        if tens_digit != 0:
            number_string += "-" + tens_string
        if ones_digit != 0:
            number_string += "-" + ones_string
    for i in range(len(sentence)):
        if sentence[i] == "$":
            sentence[i] = number_string
    print(" ".join(sentence))

main()
