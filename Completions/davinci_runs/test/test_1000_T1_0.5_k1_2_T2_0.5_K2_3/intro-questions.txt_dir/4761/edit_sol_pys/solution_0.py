

def main():
    low, high = [int(x) for x in input().split()] #split input into low and high
    num_permutations = 0
    for i in range(low, high + 1): #for i in range of low to high
        if is_valid(i):
            num_permutations += 1
    print(num_permutations) #print number of permutations

def is_valid(n): #check if valid
    n = str(n) #convert n to string
    if len(n) != 6: #if length of n is not 6
        return False
    if len(set(n)) != 6: #if length of set of n is not 6
        return False
    for i in range(1, 10):
        if n.count(str(i)) > 1: #if count of i in n is greater than 1
            return False
    for i in n:
        if int(n) % int(i) != 0: #if n mod i != 0
            return False
    return True

main() #call main function
