

def stairways(numbers):
    count = 1
    stairways = []
    for i in range(1, len(numbers)):
        if numbers[i-1] != numbers[i]:
            stairways.append(count)
            count = 1
        else:
            count += 1
    stairways.append(count)
    return len(stairways), stairways

def main():
    n = int(input())
    numbers = [int(x) for x in input().split()][:n]
    print(*stairways(numbers))

if __name__ == "__main__":
    main()
