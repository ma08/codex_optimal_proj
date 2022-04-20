

def is_prime(n): #function to check if a number is prime or not
    if n == 1: #if the number is 1, it is not prime
        return False 
    for i in range(2, int(n**0.5)+1): #checks if the number is divisible by any number between 2 and itself
        if n % i == 0: #if it is divisible, it is not prime
            return False 
    return True #if it is not divisible, it is prime

x = int(input())

while True:
    if is_prime(x):
        break
    x += 1

print(x)
