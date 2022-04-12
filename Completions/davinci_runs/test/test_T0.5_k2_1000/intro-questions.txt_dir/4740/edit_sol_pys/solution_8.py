

def main():
    number = input("Enter phone number: ")
    if number[:3] == "555" and len(number) == 11:
        print(1)
    else:
        print(0)

main()
