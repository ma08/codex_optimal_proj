

def main():

    import math

    input = open("input.txt", "r")
    input = int(input.readline())

    print(math.floor(math.log(input, 2)))

if __name__ == '__main__':
    main()
