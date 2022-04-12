
def main():
    num = int(input())
    while num > 9: 
        digits = [int(d) for d in str(num)]
        product = 1
        for d in digits:
            if d != 0:
                product *= d
        num = product
    print(num)

if __name__ == "__main__":
    main()
