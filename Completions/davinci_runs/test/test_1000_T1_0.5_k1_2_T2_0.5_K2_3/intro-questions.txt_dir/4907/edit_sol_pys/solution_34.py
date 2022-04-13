
import sys 
  
# Function to return gcd of a and b 
def gcd(a,b): 
    if a == 0 : 
        return b 
      
    return gcd(b%a, a) 
  
# Function to find gcd of array of 
# numbers 
def findGCD(arr,n): 
  
    result = arr[0] 
    for i in range(1, n): 
        result = gcd(arr[i], result) 
      
    return result 
  
# Driver program to test above function 
arr = list(map(int, input().split())) 
n = len(arr) 
print(findGCD(arr,n)) 
