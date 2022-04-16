
# Workaround for raw_input in Python 3
try:
    input = raw_input
except NameError:
    pass

def main():
    n = int(input()) # input() returns a string, so we need to convert it to int
    print(n + 1) # print() automatically adds a newline

if __name__ == "__main__":
    main()
