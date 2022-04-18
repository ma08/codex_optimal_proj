
def main():
    n = int(input("Enter a number: "))
    if n % 3 == 0:
        print("triple", n // 3)
    elif n % 2 == 0:
        print("double", n // 2)
    else:
        print("single", n)
main()
