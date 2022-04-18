

def convert(binary):
    octal = ""
    while len(binary) % 3 != 0:
        binary = "0" + binary
    for i in range(0, len(binary), 3):
        if binary[i:i+3] == "000":
            octal += "0"
        elif binary[i:i+3] == "001":
            octal += "1"
        elif binary[i:i+3] == "010":
            octal += "2"
        elif binary[i:i+3] == "011":
            octal += "3"
        elif binary[i:i+3] == "100":
            octal += "4"
        elif binary[i:i+3] == "101":
            octal += "5"
        elif binary[i:i+3] == "110":
            octal += "6"
        elif binary[i:i+3] == "111":
            octal += "7"
    return octal

def main():
    binary = input()
    print(convert(binary))

if __name__ == "__main__":
    main()
