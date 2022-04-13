
def gcd(a, b): # function to find GCD of two numbers
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b): # function to find LCM of two numbers
    return (a * b) // gcd(a, b)

def main():
    n = int(input()) # number of elements in an array 
    a = list(map(int, input().split())) # array of elements
    min_lcm = lcm(a[0], a[1]) # initializing minimum LCM
    min_i = 1
    min_j = 2
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if lcm(a[i], a[j]) < min_lcm:
                min_lcm = lcm(a[i], a[j])
                min_i = i + 1
                min_j = j + 1
    print(min_i, min_j)

if __name__ == '__main__':
    main()
