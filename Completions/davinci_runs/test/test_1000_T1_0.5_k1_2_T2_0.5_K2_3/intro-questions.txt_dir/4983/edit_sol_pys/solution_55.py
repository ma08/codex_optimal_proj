

num = int(input())

while num > 9:
    num = str(num)
    num = [str(int(i)) for i in num if i != '0']
    num = ''.join(num) 
    num = int(num) 


print(num)
