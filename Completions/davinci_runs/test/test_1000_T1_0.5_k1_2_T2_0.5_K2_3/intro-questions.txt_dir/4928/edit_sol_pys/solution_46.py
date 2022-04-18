

# Workaround for raw_input in Python3
try:
    input = raw_input
except NameError:
    pass

def main():
    print(1)

if __name__ == "__main__":
    main()
