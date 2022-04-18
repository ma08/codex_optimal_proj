

def numToWords(num):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundreds = ["", "onehundred", "twohundred", "threehundred", "fourhundred", "fivehundred", "sixhundred", "sevenhundred", "eighthundred", "ninehundred", "onethousand"]
    if num < 10:
        return ones[num]
    elif num < 20:
        return teens[num - 10]
    elif num < 100:
        return tens[num // 10] + ones[num % 10]
    elif num < 1000:
        return hundreds[num // 100]
        return hundreds[num // 100] + tens[(num // 10) % 10] + ones[num % 10]
    else:
        print("ERROR: Number too large")
        return None

def main():
    N = int(input())
    sentence = []
    for i in range(N):
        sentence.append(input())

    idx = sentence.index("$")
    num = len("".join(sentence[:idx])) + len("".join(sentence[idx+1:]))
    sentence[idx] = numToWords(num)
    print(" ".join(sentence))

if __name__ == "__main__":
    main()
