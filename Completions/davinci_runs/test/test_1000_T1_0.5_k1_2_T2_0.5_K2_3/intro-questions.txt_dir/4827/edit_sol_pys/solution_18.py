

import sys

def main():
    # read N
    N = int(sys.stdin.readline())

    # read the sentence
    sentence = []
    for i in range(N):
        sentence.append(sys.stdin.readline().strip())

    # find the position of the '$'
    pos = sentence.index('$')

    # print the sentence
    print(get_sentence(pos, sentence))

def get_sentence(pos, sentence):
    # see if we have to add anything to the number
    if pos == 0:
        number = get_number(pos, sentence)
        return str(number) + ' ' + ' '.join(sentence[pos+1:])
    elif pos == len(sentence)-1:
        number = get_number(pos, sentence)
        return ' '.join(sentence[:pos]) + ' ' + str(number)
    else:
        number = get_number(pos, sentence)
        return ' '.join(sentence[:pos]) + ' ' + str(number) + ' ' + ' '.join(sentence[pos+1:])

def get_number(pos, sentence):
    # see if we have to add anything to the number
    if pos == 0:
        number = len(' '.join(sentence[pos+1:]))
    elif pos == len(sentence)-1:
        number = len(' '.join(sentence[:pos]))
    else:
        number = len(' '.join(sentence[:pos])) + len(' '.join(sentence[pos+1:]))

    return number_to_english(number)

def number_to_english(number):
    if number == 0:
        return 'zero'
    if number == 1:
        return 'one'
    if number == 2:
        return 'two'
    if number == 3:
        return 'three'
    if number == 4:
        return 'four'
    if number == 5:
        return 'five'
    if number == 6:
        return 'six'
    if number == 7:
        return 'seven'
    if number == 8:
        return 'eight'
    if number == 9:
        return 'nine'
    if number == 10:
        return 'ten'
    if number == 11:
        return 'eleven'
    if number == 12:
        return 'twelve'
    if number == 13:
        return 'thirteen'
    if number == 14:
        return 'fourteen'
    if number == 15:
        return 'fifteen'
    if number == 16:
        return 'sixteen'
    if number == 17:
        return 'seventeen'
    if number == 18:
        return 'eighteen'
    if number == 19:
        return 'nineteen'
    if number == 20:
        return 'twenty'
    elif number == 30:
        return 'thirty'
    elif number == 40:
        return 'forty'
    elif number == 50:
        return 'fifty'
    elif number == 60:
        return 'sixty'
    elif number == 70:
        return 'seventy'
    elif number == 80:
        return 'eighty'
    elif number == 90:
        return 'ninety'
    elif number == 100:
        return 'one hundred'
    elif number == 200:
        return 'two hundred'
    elif number == 300:
        return 'three hundred'
    elif number == 400:
        return 'four hundred'
    elif number == 500:
        return 'five hundred'
    elif number == 600:
        return 'six hundred'
    elif number == 700:
        return 'seven hundred'
    elif number == 800:
        return 'eight hundred'
    elif number == 900:
        return 'nine hundred'
    elif number < 30:
        return 'twenty' + number_to_english(number-20)
    elif number < 40:
        return 'thirty' + number_to_english(number-30)
    elif number < 50:
        return 'forty' + number_to_english(number-40)
    elif number < 60:
        return 'fifty' + number_to_english(number-50)
    elif number < 70:
        return 'sixty' + number_to_english(number-60)
    elif number < 80:
        return 'seventy' + number_to_english(number-70)
    elif number < 90:
        return 'eighty' + number_to_english(number-80)
    elif number < 100:
        return 'ninety' + number_to_english(number-90)
    elif number < 200:
        return 'one hundred' + number_to_english(number-100)
    elif number < 300:
        return 'two hundred' + number_to_english(number-200)
    elif number < 400:
        return 'three hundred' + number_to_english(number-300)
    elif number < 500:
        return 'four hundred' + number_to_english(number-400)
    elif number < 600:
        return 'five hundred' + number_to_english(number-500)
    elif number < 700:
        return 'six hundred' + number_to_english(number-600)
    elif number < 800:
        return 'seven hundred' + number_to_english(number-700)
    elif number < 900:
        return 'eight hundred' + number_to_english(number-800)
    elif number < 1000:
        return 'nine hundred' + number_to_english(number-900)

if __name__ == '__main__':
    main()
