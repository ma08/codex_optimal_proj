

num = int(input())

while num > 9:
    num = str(num)
    num = [int(i) for i in num]
    num = [i for i in num if i != 0]
    num = [str(i) for i in num]
    num = ''.join(num)
    num = int(num)

print(num)