
import sys

def is_hard_to_enter(code):
    """
    Returns True if the code is hard to enter, False otherwise.
    """
    for i in range(len(code) - 1):
        if code[i] == code[i+1]:
            return True
    return False

def main():
    code = sys.stdin.readline().rstrip() # readline() reads a single line from the file; a newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline.
    if is_hard_to_enter(code):
        print("Bad")
    else:
        print("Good")

if __name__ == "__main__":
    main()
