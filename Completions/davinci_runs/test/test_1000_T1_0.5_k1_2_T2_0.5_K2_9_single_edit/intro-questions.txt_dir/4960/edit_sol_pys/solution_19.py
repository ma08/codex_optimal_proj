def convert(number):
    if number == "000":
        return "0"
    elif number == "001":
        return "1"
    elif number == "010":
        return "2"
    elif number == "011":
        return "3"
    elif number == "100":
        return "4"
    elif number == "101":
        return "5"
    elif number == "110":
        return "6"
    elif number == "111":
        return "7"
    else:
        return "error"

def main():
    binary = input()
    octal = ""
    while len(binary) % 3 != 0:
        binary = "0" + binary
    for i in range(0, len(binary), 3):
        octal += convert(binary[i:i+3])
    print(octal)

if __name__ == "__main__":
    main()
