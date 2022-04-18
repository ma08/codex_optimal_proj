

numbers = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20,'thirty':30,'forty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90,'onehundred':100,'twohundred':200,'threehundred':300,'fourhundred':400,'fivehundred':500,'sixhundred':600,'sevenhundred':700,'eighthundred':800,'ninehundred':900}

N = int(input())

words = []

for i in range(N):
    words.append(input())

sentence = ''

for word in words:
    sentence += word + ' '

num = sentence.split('$')

num[0] = num[0].split()
num[1] = num[1].split()

num[0] = len(num[0])
num[1] = len(num[1])

total = num[0] + num[1]

if total >= 100:
    if total%100 == 0:
        hundreds = total//100
        hundreds = str(numbers[str(hundreds)]) + 'hundred'
        print(hundreds)
    else:
        hundreds = total//100
        total -= hundreds*100
        hundreds = str(numbers[str(hundreds)]) + 'hundred' + 'and'
        if total > 20:
            tens = total//10
            total -= tens*10
            tens = str(numbers[tens])
            ones = str(numbers[total])
            print(hundreds + ' ' + tens + ' ' + ones)
        else:
            total = str(numbers[total])
            print(hundreds + ' ' + total)
elif total > 20:
    tens = total//10
    total -= tens*10
    tens = str(numbers[tens])
    ones = str(numbers[total])
    print(tens + ' ' + ones)
else:
    total = str(numbers[total])
    print(total)
