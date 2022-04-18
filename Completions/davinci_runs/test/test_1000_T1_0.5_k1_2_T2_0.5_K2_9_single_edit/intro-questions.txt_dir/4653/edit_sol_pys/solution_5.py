import sys

def main():
    """
    Main Function
    """
    num_cases = int(sys.stdin.readline()) #number of test cases
    for _ in range(num_cases): #iterate over test cases
        n, k = [int(x) for x in sys.stdin.readline().split()] #read in two numbers
        if n < k: #if the number of digits is less than the number of digits we can remove
            print(n) #print the number of digits
        else:
            print((n // k) * k + min(k // 2, n % k)) #print the number of digits after removing digits

if __name__ == "__main__":
    main() #call main function
