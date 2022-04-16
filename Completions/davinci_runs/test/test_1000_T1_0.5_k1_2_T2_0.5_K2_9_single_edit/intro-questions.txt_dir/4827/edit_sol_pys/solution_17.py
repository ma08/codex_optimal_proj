

def name(n):
    if n == 0:
        return ''
    if n == 1:
        return 'one'
    if n == 2:
        return 'two'
    if n == 3:
        return 'three'
    if n == 4:
        return 'four'
    if n == 5:
        return 'five'
    if n == 6:
        return 'six'
    if n == 7:
        return 'seven'
    if n == 8:
        return 'eight'
    if n == 9:
        return 'nine'
    if n == 10:
        return 'ten'
    if n == 11:
        return 'eleven'
    if n == 12:
        return 'twelve'
    if n == 13:
        return 'thirteen'
    if n == 14:
        return 'fourteen'
    if n == 15:
        return 'fifteen'
    if n == 16:
        return 'sixteen'
    if n == 17:
        return 'seventeen'
    if n == 18:
        return 'eighteen'
    if n == 19:
        return 'nineteen'
    if n == 20:
        return 'twenty'
    if n == 30:
        return 'thirty'
    if n == 40:
        return 'forty'
    if n == 50:
        return 'fifty'
    if n == 60:
        return 'sixty'
    if n == 70:
        return 'seventy'
    if n == 80:
        return 'eighty'
    if n == 90:
        return 'ninety'
    if n == 100:
        return 'onehundred'
    if n == 200:
        return 'twohundred'
    if n == 300:
        return 'threehundred'
    if n == 400:
        return 'fourhundred'
    if n == 500:
        return 'fivehundred'
    if n == 600:
        return 'sixhundred'
    if n == 700:
        return 'sevenhundred'
    if n == 800:
        return 'eighthundred'
    if n == 900:
        return 'ninehundred'
    if n%100 == 0:
        return name(n//100) + 'hundred'
    if n < 100:
        return name(n//10*10) + name(n%10)
    return name(n//100) + 'hundred' + name(n%100)

def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())

    total = 0
    for word in words:
        if word != '$':
            total += len(word)
        else:
            words[words.index(word)] = name(total)

    print(' '.join(words))

if __name__ == '__main__':
    main()
