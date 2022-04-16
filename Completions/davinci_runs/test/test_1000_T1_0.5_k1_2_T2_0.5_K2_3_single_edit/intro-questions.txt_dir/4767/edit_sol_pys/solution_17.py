
import sys

def compute(registers, max_value):
    # how many more operations can we do?
    # if we can't do any more, we're done
    if registers[-1] == max_value:
        return 0
    # otherwise, we can do at least one more
    # the question is how many more can we do?
    # we can do as many more as we can increment the least significant register
    # without overflowing
    return max_value + 1 - registers[0]

def main():
    registers = [int(x) for x in sys.stdin.readline().split()]
    print(compute(registers, 18))

if __name__ == '__main__':
    main()
