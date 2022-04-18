

num = int(input())

while num > 9:
    num = str(num)
    num = [int(i) for i in num]
    num = [i for i in num if i != 0 and i != 1]
    num = [str(i) for i in num]
    print(num)
    num = ''.join(num).strip()
    if num == '':
        num = 0
    else:
        num = int(num)

print(num)
