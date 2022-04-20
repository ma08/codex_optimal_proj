

#-----Solution-----

#This solution uses a formula to calculate the value of the digit at a given position

#The value of the digit at a given position is calculated by finding the block in which the digit is present
#and then finding the position of the digit within the block

#The value of the digit at a given position can be calculated by finding the value of the digit at the start of the block
#and then adding the position of the digit within the block

#The value of the digit at the start of the block can be calculated by finding the sum of the digits of all the numbers from 1 to the block number

#The sum of the digits of all the numbers from 1 to n can be calculated by using the formula (1+n)*n/2

#The block in which the digit is present can be calculated by finding the value of n for which (1+n)*n/2 is less than or equal to the position

#The position of the digit within the block can be calculated by finding the difference between the position and the value of the digit at the start of the block

#The following code implements the above algorithm

q = int(input())

for i in range(q):
    k = int(input())
    n = int(((-1+((1+8*k)**0.5))/2)//1)
    print(str((1+n)*n//2-k)[-1])