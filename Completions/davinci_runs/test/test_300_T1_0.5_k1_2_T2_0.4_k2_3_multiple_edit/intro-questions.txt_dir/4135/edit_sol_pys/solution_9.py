

def s(n): #function to find the divisor
   for i in range(n,0,-1): #loop to find the divisor
       if n%i == 0: #condition to check if the value is divisor
           return i #return the value

def main():
    n = int(input()) #input the value
    t = input() #input the string
    d = s(n) #find the divisor
    print(t[d:], end="") #print the string
    print(t[:d][::-1], end="") #print the string

main()
