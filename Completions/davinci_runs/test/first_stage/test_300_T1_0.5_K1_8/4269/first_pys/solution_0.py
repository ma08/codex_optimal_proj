

import sys

def main():
    code = input()
    if code[0] == code[1] or code[1] == code[2] or code[2] == code[3]:
        print("Bad")
    else:
        print("Good")

if __name__ == "__main__":
    main()