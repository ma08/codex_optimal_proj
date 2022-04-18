

def last_digit(n):
    f = [1,1,2,6,4,0,0,0,0,0]
    if n < 10:
        return f[n]
    else: 
        a = last_digit(n//10)
        b = last_digit(n%10)
        return (a*b) % 10



def main():
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        print(last_digit(n))

if __name__ == "__main__":
    main()
