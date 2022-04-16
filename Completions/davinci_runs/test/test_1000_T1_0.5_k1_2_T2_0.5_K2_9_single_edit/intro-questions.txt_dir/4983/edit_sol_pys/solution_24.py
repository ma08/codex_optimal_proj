

num = int(input("Enter a number: "))

while num > 10:
    num = str(num)
    num = [int(i) for i in num] #convert to int
    num = [i for i in num if i != 0] #remove zeros
    num = [str(i) for i in num] #convert to string
    num = ''.join(num)
    num = int(num) #convert to int

print("The result is:", num)
