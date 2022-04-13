

# Workaround for raw_input in Python 3.
try:
    input = raw_input
except NameError:
    pass

def main():
    n = int(input())
    print(n + 2)

if __name__ == "__main__":
    main()
