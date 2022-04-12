
def convert(number):
    return {
        "000": "0",
        "001": "1",
        "010": "2",
        "011": "3",
        "100": "4",
        "101": "5",
        "110": "6",
        "111": "7",
    }[number]


def main():
    binary = input("Enter the binary number: ")
    octal = ""
    while len(binary) % 3 != 0:
        binary = "0" + binary
    for i in range(0, len(binary), 3):
        octal += convert(binary[i:i + 3])
    print(octal)


if __name__ == "__main__":
    main()
