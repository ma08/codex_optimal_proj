

import sys

def main():
    # Read the number of files
    N = int(sys.stdin.readline()) 

    # Read the lengths of the files
    files = []
    for i in range(N):
        files.append(int(sys.stdin.readline()))

    # Sort the files from shortest to longest
    files.sort()

    # Iterate over the files
    while len(files) > 1:
        # Fuse the two shortest files
        files[0] = files[0] + files[1] - 1
        # Remove the second shortest file
        del files[1]
        # Sort the files from shortest to longest
        files.sort()

    # Print the length of the resulting file 
    print(files[0])

if __name__ == "__main__":
    main()
