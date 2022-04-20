
import sys

def is_hard_to_enter(code):
    """
    Returns True if the code is hard to enter, False otherwise.
    """
    for i in range(1, len(code)):
        if code[i] == code[i - 1]:
            return True
    return False

def main():
    code = sys.stdin.readline().rstrip()
    if is_hard_to_enter(code):
        print("Bad")
    else:
        print("Good")

if __name__ == "__main__":
    main()
