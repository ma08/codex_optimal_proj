
def find_index(arr):
    max_temp = []
    for i in range(len(arr) - 2):
        max_temp.append(max(arr[i], arr[i + 1], arr[i + 2]))
    index = max_temp.index(min(max_temp))
    return index + 1, max_temp[index]



import sys

def main():
    n = int(sys.stdin.readline().strip())
    temp = [int(i) for i in sys.stdin.readline().strip().split()]
    print(find_index(temp))


if __name__ == '__main__':
    main()
