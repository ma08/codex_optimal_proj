import math

def main():
    V = int(input())

    for i in range(2, int(math.sqrt(V)) + 1):
        if V % i == 0:

            print(2 * (V // i + i))
            break

if __name__ == "__main__":
    main()
