
# 
import sys

def main():
    n = int(sys.stdin.readline())
    arr = [int(x) for x in sys.stdin.readline().split()]
    result = []
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if arr[i] == arr[j]:
                result.append([i, j])
                i = j
                j = i + 1
            else:
                j += 1
        result.append([i, i])
        i += 1
    print(len(result))
    for r in result:
        print(str(r[0] + 1) + " " + str(r[1] + 1))

if __name__ == "__main__":
    main()
