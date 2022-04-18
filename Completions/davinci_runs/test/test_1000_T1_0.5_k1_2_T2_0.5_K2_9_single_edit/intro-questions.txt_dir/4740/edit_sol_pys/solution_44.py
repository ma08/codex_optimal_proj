

def main():
    number = input("Enter number")
    if number[:3] == "555" and len(number) == 10:
        print(1)
    else:
        print(0)

main()
