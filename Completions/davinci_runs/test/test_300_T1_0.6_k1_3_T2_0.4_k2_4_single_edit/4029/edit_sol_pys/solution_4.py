

n = int(input())

def mod25(n):
    if n % 25 == 0:
        return True
    else:
        return False

def swap_adjacent(n):
    n = str(n) # convert to string
    n1 = n[0]
    n2 = n[1]
    n = n2 + n1 + n[2:] # swap adjacent numbers
    return n

def main():
    n = str(n) # convert to string
    counter = 0
    while(len(n) > 2): # while length of string is greater than 2
        if mod25(int(n)):
            break # if it is divisible by 25, stop
        else:
            n = swap_adjacent(n) # swap adjacent numbers
            counter += 1
    if mod25(int(n)): # if it is divisible by 25
        print(counter)
    else: # else, print -1
        print(-1)

main()
