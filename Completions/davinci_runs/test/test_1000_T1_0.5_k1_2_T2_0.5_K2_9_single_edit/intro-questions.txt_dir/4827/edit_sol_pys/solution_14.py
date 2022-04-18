

import sys
    print('hello')
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
    elif number == 1:
        return 'one'
    elif number == 2:
        return 'two'
    elif number == 3:
        return 'three'
    elif number == 4:
        return 'four'
    elif number == 5:
        return 'five'
    elif number == 6:
        return 'six'
    elif number == 7:
        return 'seven'
    elif number == 8:
        return 'eight'
    elif number == 9:
        return 'nine'
    elif number == 10:
        return 'ten'
    elif number == 11:
        return 'eleven'
    elif number == 12:
        return 'twelve'
    elif number == 13:
        return 'thirteen'
    elif number == 14:
        return 'fourteen'
    elif number == 15:
        return 'fifteen'
    elif number == 16:
        return 'sixteen'
    elif number == 17:
        return 'seventeen'
    elif number == 18:
        return 'eighteen'
    elif number == 19:
        return 'nineteen'
    elif number == 20:
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
        return 'onehundred'
    elif number == 200:
        return 'twohundred'
    elif number == 300:
        return 'threehundred'
    elif number == 400:
        return 'fourhundred'
    elif number == 500:
        return 'fivehundred'
    elif number == 600:
        return 'sixhundred'
    elif number == 700:
        return 'sevenhundred'
    elif number == 800:
        return 'eighthundred'
    elif number == 900:
        return 'ninehundred'
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
        return 'onehundred' + number_to_english(number-100)
    elif number < 300:
        return 'twohundred' + number_to_english(number-200)
    elif number < 400:
        return 'threehundred' + number_to_english(number-300)
    elif number < 500:
        return 'fourhundred' + number_to_english(number-400)
    elif number < 600:
        return 'fivehundred' + number_to_english(number-500)
    elif number < 700:
        return 'sixhundred' + number_to_english(number-600)
    elif number < 800:
        return 'sevenhundred' + number_to_english(number-700)
    elif number < 900:
        return 'eighthundred' + number_to_english(number-800)
    elif number < 1000:
        return 'ninehundred' + number_to_english(number-900)

if __name__ == '__main__':
    main()
