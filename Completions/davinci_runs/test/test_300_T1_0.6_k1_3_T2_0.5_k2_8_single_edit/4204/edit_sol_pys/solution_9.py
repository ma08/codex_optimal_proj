

s = input()
k = int(input())

def calc(s, k):
    for i in range(k):
        s = s.replace('2', '22')
        s = s.replace('3', '33')
        s = s.replace('4', '44')
        s = s.replace('5', '55')
        s = s.replace('6', '66')
        s = s.replace('7', '77')
        s = s.replace('8', '88')
        s = s.replace('9', '99')
    return s

print(calc(s, k)[k-1])
