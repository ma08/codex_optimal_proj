

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
        return 'one hundred'
    if n == 200:
        return 'two hundred'
    if n == 300:
        return 'three hundred'
    if n == 400:
        return 'four hundred'
    if n == 500:
        return 'five hundred'
    if n == 600:
        return 'six hundred'
    if n == 700:
        return 'seven hundred'
    if n == 800:
        return 'eight hundred'
    if n == 900:
        return 'nine hundred'
    if n%100 == 0:
        return name(n//100) + ' hundred'
    if n < 100:
        return name(n//10*10) + ' ' + name(n%10)
    return name(n//100) + ' hundred and ' + name(n%100)

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
