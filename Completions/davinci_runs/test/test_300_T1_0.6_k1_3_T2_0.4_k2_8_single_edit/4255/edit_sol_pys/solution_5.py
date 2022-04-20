
import math

def main():
    a, b, c = input("Enter three numbers: ").split()
    a, b, c = int(a), int(b), int(c)  # convert to int
    s = (a + b + c) / 2  # calculate s
    print(math.sqrt(s * (s - a) * (s - b) * (s - c)))  # calculate area

if __name__ == "__main__":
    main()
