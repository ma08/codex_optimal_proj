import math

def main():
    s = input()
    print(s[:math.ceil(len(s) / 2)])

if __name__ == "__main__":
    main()
