

def main():
    n, c = map(int, input().split())  # n is the number of elements in the array, c is the number of colors
    nums = list(map(int, input().split()))
    freq = [0] * (c + 1)  # frequency of each color
    for i in nums:
        freq[i] += 1  # incrementing the frequency of the color
    for i in range(1, c + 1):
        print((str(i) + " ") * freq[i], end="")  # printing the color i freq[i] times
    print()

if __name__ == '__main__':
    main()
