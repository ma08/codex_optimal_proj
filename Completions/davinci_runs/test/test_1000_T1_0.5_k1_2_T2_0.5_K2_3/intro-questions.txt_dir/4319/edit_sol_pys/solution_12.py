
def stairways(numbers):
    count = 1
    stairways_count = []
    for i in range(1, len(numbers)):
        if numbers[i-1] != numbers[i]:
            stairways_count.append(count)
            count = 1
        else:
            count += 1
    stairways_count.append(count)
    return len(stairways_count), stairways_count

def main():
    n = int(input())
    numbers = [int(x) for x in input().split()]
    print(*stairways(numbers))

if __name__ == "__main__":
    main()
