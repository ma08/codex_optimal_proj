
import re

if __name__ == '__main__':
    S = input()
    if re.search(r'^[a-zA-Z]', S):
        print("yes")
    else:
        print("no")
