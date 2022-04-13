

def main():
    # Read the input
    s = sys.stdin.readline()
    s = s.replace("+","\n")
    s = s.split("\n")

    # Convert the input to a list of integers
    for i in range(len(s)):
        s[i] = int(s[i])

    # Count the number of ways the list can be evaluated
    count = 0
    for i in range(1,len(s)):
        count += len(s) - i
    print(count)

if __name__ == "__main__":
    main()
