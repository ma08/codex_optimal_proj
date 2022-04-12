import sys

def main():
    n = int(sys.stdin.readline().strip())
    numbers = []
    for i in range(n):
        numbers.append(int(sys.stdin.readline().strip()))
    numbers = set(numbers)
    if len(numbers) == numbers[-1]: # if the length of the set is the same as the last element in the set
        print("good job")
    else:
        for i in range(1,numbers[-1]+1): # if the length of the set is not the same as the last element in the set
            if i not in numbers:
                print(i)

if __name__ == '__main__':
    main()
