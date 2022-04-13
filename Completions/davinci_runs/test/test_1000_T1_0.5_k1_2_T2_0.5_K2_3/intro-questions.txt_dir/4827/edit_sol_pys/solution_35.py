

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
        number_string = "Zero"
    elif number < 11:
        number_string = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"][number - 1]
    elif number < 20:
        number_string = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"][number - 11]
    elif number < 100:
        tens_digit = number // 10
        ones_digit = number % 10
        tens_string = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"][tens_digit - 2]
        ones_string = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"][ones_digit - 1]
        number_string = tens_string
        if ones_digit != 0:
            number_string += " " + ones_string
    else:
        hundreds_digit = number // 100
        tens_digit = (number % 100) // 10
        ones_digit = (number % 100) % 10
        hundreds_string = ["OneHundred", "TwoHundred", "ThreeHundred", "FourHundred", "FiveHundred", "SixHundred", "SevenHundred", "EightHundred", "NineHundred"][hundreds_digit - 1]
        tens_string = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"][tens_digit - 2]
        ones_string = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"][ones_digit - 1]
        number_string = hundreds_string
        if tens_digit != 0:
            number_string += " " + tens_string
        if ones_digit != 0:
            number_string += " " + ones_string
    for i in range(len(sentence)):
        if sentence[i] == "$":
            sentence[i] = number_string
    print(" ".join(sentence))

main()
