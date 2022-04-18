

def main():
    # Get input and remove the first line
    lines = [line.rstrip('\n') for line in open('input.txt')]
    lines.pop(0)

    # Solve each line
    for line in lines:
        # Solve
        print(solve(line))

def solve(line):
    # Get the first and second numbers
    nums = line.split()
    first = int(nums[0])
    second = int(nums[1])

    # Return the answer
    return first + second


if __name__ == '__main__':
    main()
