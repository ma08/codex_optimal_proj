

s = input()
k = int(input())

def calc(s, k):
    for i in range(k):
        s = s.replace('2', '22', 1)
        s = s.replace('3', '333', 1)
        s = s.replace('4', '4444', 1)
        s = s.replace('5', '55555', 1)
        s = s.replace('6', '666666', 1)
        s = s.replace('7', '7777777', 1)
        s = s.replace('8', '88888888', 1)
        s = s.replace('9', '999999999', 1)
    return s

print(calc(s, k)[k-1])
