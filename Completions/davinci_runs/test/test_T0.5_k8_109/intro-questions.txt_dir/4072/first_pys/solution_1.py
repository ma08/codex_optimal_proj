
import math

def check_armstrong(a):
    sum = 0
    for i in str(a):
        sum += math.pow(int(i), 3)
    if sum == a:
        return 1
    else:
        return 0

if __name__ == "__main__":
    print(check_armstrong(int(input())))