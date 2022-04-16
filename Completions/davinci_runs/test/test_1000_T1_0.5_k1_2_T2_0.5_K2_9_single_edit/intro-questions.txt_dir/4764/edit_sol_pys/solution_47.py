import math



def main():
    n = int(input())
    h = int(input())
    v = int(input())

    volume = (n - max(h, n - h)) * (n - max(v, n - v)) * math.pi


    print(volume)

if __name__ == "__main__":
    main()
