
import sys

def main():
    # Read the number of lines
    N = int(sys.stdin.readline()) - 1

    # Read the lines
    lines = []
    for i in range(1, N + 1):
        lines.append(sys.stdin.readline())

    # Read the text to be searched
    text = sys.stdin.readline()

    # Iterate over the lines
    for line in lines:
        # Check if the text is in the line
        if text in line:
            # Print the line
            print(line.strip())


if __name__ == "__main__":
    main()
