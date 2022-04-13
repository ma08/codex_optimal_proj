

n = int(input())

if n % 3 != 0:
    print("impossible") # if the number is not divisible by 3, it is impossible to get the number with any combination of doubles and triples
else:
    n //= 3 # if the number is divisible by 3, we can start with a triple
    if n > 20:
        print("triple", n // 3) # if the number is still greater than 20, we can add more triples and print them
        n = n % 3
    if n > 20:
        print("triple", n // 3) # if the number is still greater than 20, we can add more triples and print them
        n = n % 3
    if n > 20:
        print("triple", n // 3) # if the number is still greater than 20, we can add more triples and print them
        n = n % 3
    if n > 20:
        print("impossible")
    else:
        if n % 2 == 0:
            print("double", n // 2)
        else:
            print("single", n)
