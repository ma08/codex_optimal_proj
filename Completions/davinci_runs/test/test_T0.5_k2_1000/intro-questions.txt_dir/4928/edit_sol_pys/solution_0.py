
# Workaround for raw_input in Python 3.
try:
    input = raw_input
except NameError:
    pass

def main():
    print(int(input()) + 1)

if __name__ == "__main__":
    main()
