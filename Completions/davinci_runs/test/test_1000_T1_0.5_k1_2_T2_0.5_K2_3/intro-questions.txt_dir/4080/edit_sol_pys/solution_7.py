

def solve(numbers, commands):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    pass

if __name__ == '__main__':
    numbers_count, commands_count = [int(i) for i in input().split()]
    numbers = [int(i) for i in input().split()]
    commands = []
    for i in range(commands_count):
        commands.append([int(i) for i in input().split()])
    solve(numbers, commands)
