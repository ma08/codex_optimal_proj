from math import sqrt

def area(a, b, c, d):
    s = (a + b + c + d) / 2
    return sqrt((s - a) * (s - b) * (s - c) * (s - d))

def main():
    a = [int(x) for x in input().split()] 
    a.sort()
    print(max(area(a[0], a[1], a[2], a[3]), area(a[0], a[1], a[2], a[0] + a[1] + a[2])))

if __name__ == "__main__":
    main()
