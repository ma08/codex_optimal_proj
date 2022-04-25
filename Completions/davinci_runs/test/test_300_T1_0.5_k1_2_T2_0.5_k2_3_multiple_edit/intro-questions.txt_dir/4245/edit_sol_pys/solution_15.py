
import math #import math module to use ceil function

def minPowerStrips(A, B): #function to calculate the minimum number of power strips
    return math.ceil(B / A) #calculate the number of power strips and round up to nearest integer

def main(): #function to take input and call the function
    line = input().split() #take input and split it into two variables
    A = int(line[0]) #convert the first variable to an integer
    B = int(line[1]) #convert the second variable to an integer
    print(minPowerStrips(A, B)) #call the function and print the result

if __name__ == '__main__': #call the function main
    main()
