

def check_valid(a,b,c):
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False

def area(a,b,c):
    s = (a + b + c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5

if __name__ == "__main__":
    a,b,c = map(int,input().split())
    if check_valid(a,b,c):
        print(area(a,b,c))
    else:
        print("Invalid")
